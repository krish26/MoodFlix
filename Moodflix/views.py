"""
Views for the movie recommender using procedural ML setup (no class)
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import pickle
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Global data
_movies_df = None
_content_matrix = None
_cosine_sim_matrix = None
_scaler = MinMaxScaler()

# ---------------------------
# Load ML model & movie data
# ---------------------------
def load_ml_model():
    global _movies_df, _content_matrix, _cosine_sim_matrix, _scaler

    if _movies_df is None:
        print("Loading ML model...")

        movies_file = os.path.join(settings.BASE_DIR, "data", "processed_movies.pkl")
        model_file = os.path.join(settings.BASE_DIR, "data", "pl1")

        # Load movie data
        with open(movies_file, "rb") as f:
            _movies_df = pickle.load(f)

        # Load model data
        if os.path.exists(model_file):
            with open(model_file, "rb") as f:
                model_data = pickle.load(f)
            _content_matrix = model_data["content_matrix"]
            _cosine_sim_matrix = model_data["cosine_sim_matrix"]
            _scaler = model_data["scaler"]
            print("ML model loaded successfully")
        else:
            raise FileNotFoundError("ML model not found. Train the model first.")

    return _movies_df, _content_matrix, _cosine_sim_matrix, _scaler

# ---------------------------
# Utility: Format movie
# ---------------------------
def format_movie_row(movie_row):
    return {
        "id": int(movie_row["id"]),
        "title": movie_row["title"],
        "overview": movie_row.get("overview", ""),
        "genres": movie_row.get("genre_names", []),
        "rating": float(movie_row.get("vote_average", 0)),
        "vote_count": int(movie_row.get("vote_count", 0)),
        "release_date": str(movie_row.get("release_date", "")),
        "runtime": int(movie_row["runtime"]) if "runtime" in movie_row and movie_row["runtime"] else None,
        "cast": movie_row.get("cast_names", [])[:5],
        "director": movie_row.get("director", ""),
        "poster_path": movie_row.get("poster_path", ""),
    }

# ---------------------------
# Mood-based recommendation
# ---------------------------
def get_mood_based_recommendations_proc(movies_df, cosine_sim_matrix, scaler, mood, n=5, diversity_factor=0.3):
    mood_col = f"mood_{mood}_score"
    if mood_col not in movies_df.columns:
        return []

    # Top candidates by mood
    candidates_df = movies_df.nlargest(n*5, mood_col).copy()

    candidates_df["mood_score_norm"] = scaler.fit_transform(candidates_df[[mood_col]])
    candidates_df["rating_score_norm"] = scaler.fit_transform(candidates_df[["vote_average"]])
    candidates_df["popularity_score_norm"] = scaler.fit_transform(candidates_df[["popularity"]])

    candidates_df["composite_score"] = (
        0.5*candidates_df["mood_score_norm"] +
        0.3*candidates_df["rating_score_norm"] +
        0.2*candidates_df["popularity_score_norm"]
    )

    # Select diverse movies
    selected_indices = []
    remaining_indices = list(range(len(candidates_df)))
    if not remaining_indices:
        return []

    selected_indices.append(0)
    remaining_indices.remove(0)

    while len(selected_indices) < n and remaining_indices:
        max_score = -1
        best_idx = None

        for idx in remaining_indices:
            candidate_idx = candidates_df.iloc[idx].name
            similarities = []
            for sel_idx in selected_indices:
                sel_movie_idx = candidates_df.iloc[sel_idx].name
                if candidate_idx < len(cosine_sim_matrix) and sel_movie_idx < len(cosine_sim_matrix):
                    similarities.append(cosine_sim_matrix[candidate_idx][sel_movie_idx])
            avg_sim = np.mean(similarities) if similarities else 0
            diversity_score = 1 - avg_sim
            position_score = 1 - (idx / len(candidates_df))
            combined_score = (1 - diversity_factor)*position_score + diversity_factor*diversity_score

            if combined_score > max_score:
                max_score = combined_score
                best_idx = idx

        if best_idx is not None:
            selected_indices.append(best_idx)
            remaining_indices.remove(best_idx)

    return [candidates_df.iloc[i].name for i in selected_indices]

# ---------------------------
# Django Views
# ---------------------------

def index(request):
    moods = [
        "happy", "sad", "excited", "scared", "romantic",
        "thoughtful", "adventurous", "relaxed", "mysterious", "inspired"
    ]
    return render(request, "Moodflix/index.html", {"moods": moods})


@require_http_methods(["GET"])
def get_moods(request):
    moods = [
        "happy", "sad", "excited", "scared", "romantic",
        "thoughtful", "adventurous", "relaxed", "mysterious", "inspired"
    ]
    return JsonResponse({"success": True, "moods": moods})


@csrf_exempt
@require_http_methods(["POST"])
def get_recommendations(request):
    try:
        data = json.loads(request.body)
        mood = data.get("mood")
        count = data.get("count", 5)
        diversity = data.get("diversity", 0.3)

        if not mood:
            return JsonResponse({"success": False, "error": "Mood is required"}, status=400)

        # Load ML data
        movies_df, content_matrix, cosine_sim_matrix, scaler = load_ml_model()

        recommended_indices = get_mood_based_recommendations_proc(
            movies_df, cosine_sim_matrix, scaler, mood, n=count, diversity_factor=diversity
        )

        recommendations = [format_movie_row(movies_df.iloc[idx]) for idx in recommended_indices]

        return JsonResponse({
            "success": True,
            "mood": mood,
            "count": len(recommendations),
            "recommendations": recommendations,
            "ml_powered": True
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
