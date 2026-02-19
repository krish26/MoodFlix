
import os
import sys
import django
import pickle
from datetime import datetime

#setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')
django.setup()

from Moodflix.models import Movie

def load_movies_from_pickle(pickle_path='Data/processed_movies.pkl'):
    print('Loading movies from pickle file...')

    try:
        with open(pickle_path,'rb') as f:
            movie_df=pickle.load(f)
    except FileNotFoundError:
        print(f'error:{pickle_path} not found')
        return
    print(f'found {len(movie_df)} movies in pickle file')


    #clear existing movie
    print('Clearing exixting movies in database...')
    Movie.objects.all().delete()

    #batch insert movies

    movies_to_create =[]

    for idx,row in movie_df.iterrows():
        try:
            #parse release data
            release_date=None
            if 'release_date' in row and row['release_date']:
                try:
                    release_date=datetime.strptime(row['release_date'],'%Y-%m-%d').date()
                except ValueError:
                    print(f'warning: invalid release date format for movie {row["title"]}: {row["release_date"]}')
                    release_date=None
            movie=Movie(
                tmdb_id=int(row['id']),
                title=row['title'],
                overview=row.get('overview', ''),
                release_date=release_date,
                runtime=int(row['runtime']) if 'runtime' in row and row['runtime'] else None,
                vote_average=float(row['vote_average']),
                vote_count=int(row['vote_count']),
                popularity=float(row.get('popularity', 0)),
                poster_path=row.get('poster_path', ''),
                genres=row.get('genre_names', []) if isinstance(row.get('genre_names'), list) else [],
                cast=row.get('cast_names', []) if isinstance(row.get('cast_names'), list) else [],
                director=row.get('director', ''),
                mood_happy=float(row.get('mood_happy_score', 0)),
                mood_sad=float(row.get('mood_sad_score', 0)),
                mood_excited=float(row.get('mood_excited_score', 0)),
                mood_scared=float(row.get('mood_scared_score', 0)),
                mood_romantic=float(row.get('mood_romantic_score', 0)),
                mood_thoughtful=float(row.get('mood_thoughtful_score', 0)),
                mood_adventurous=float(row.get('mood_adventurous_score', 0)),
                mood_relaxed=float(row.get('mood_relaxed_score', 0)),
                mood_mysterious=float(row.get('mood_mysterious_score', 0)),
                mood_inspired=float(row.get('mood_inspired_score', 0)),
            )

            movies_to_create.append(movie)

            #batch insert every 100 movies

            if len(movies_to_create) >=100:
                Movie.objects.bulk_create(movies_to_create)
                print(f'Inserted {idx +1}/{len(movie_df)} movies...')
                movies_to_create=[]
        except Exception as e:
            print(f'error processing  movies')
            continue
    #insert rem movies
    if movies_to_create:
        Movie.objects.bulk_create(movies_to_create)
        
    total_count = Movie.objects.count()
    print(f'\n successfully loaded {total_count} movies into database')

if __name__=='__main__':
    load_movies_from_pickle()
               

            

