const TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p/w500';
let selectedMood = null;

const moodData = {
    happy: { icon: 'bi-emoji-smile', name: 'Happy' },
    sad: { icon: 'bi-emoji-frown', name: 'Sad' },
    excited: { icon: 'bi-lightning-charge', name: 'Excited' },
    scared: { icon: 'bi-exclamation-triangle', name: 'Scared' },
    romantic: { icon: 'bi-heart-fill', name: 'Romantic' },
    thoughtful: { icon: 'bi-lightbulb', name: 'Thoughtful' },
    adventurous: { icon: 'bi-compass', name: 'Adventurous' },
    relaxed: { icon: 'bi-cup-hot', name: 'Relaxed' },
    mysterious: { icon: 'bi-incognito', name: 'Mysterious' },
    inspired: { icon: 'bi-stars', name: 'Inspired' }
};

// Render horizontal moods
function renderMoods() {
    const moodGrid = document.getElementById('moodGrid');
    Object.keys(moodData).forEach(mood => {
        const card = document.createElement('div');
        card.className = 'mood-card';
        card.innerHTML = `<div class="mood-icon"><i class="bi ${moodData[mood].icon}"></i></div><div>${moodData[mood].name}</div>`;
        moodGrid.appendChild(card);

        card.onclick = function() {
            document.querySelectorAll('.mood-card').forEach(c => c.classList.remove('active'));
            this.classList.add('active');
            selectedMood = mood;
            document.getElementById('getRecommendationsBtn').disabled = false;
        };
    });
}

async function getRecommendations() {
    if (!selectedMood) return;
    showLoading();

    // Example API call (replace with your backend)
    const response = await fetch('/recommendations/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mood: selectedMood, count: 10 })
    });
    const data = await response.json();

    if (data.success) {
        displayResults(data.recommendations, selectedMood.toUpperCase() + " Picks");
    }
}

function displayResults(movies, title) {
    document.getElementById('emptyState').style.display = 'none';
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('resultsArea').style.display = 'block';
    document.getElementById('resultsTitle').textContent = title;

    const grid = document.getElementById('moviesGrid');
    grid.innerHTML = '';

    movies.forEach(movie => {
        const card = document.createElement('div');
        card.className = 'movie-card';

        const poster = movie.poster_path 
            ? `<img src="${TMDB_IMAGE_BASE + movie.poster_path}">` 
            : `<div style="height:300px;background:#222;"></div>`;

        const truncatedOverview = movie.overview
            ? movie.overview.length > 120
                ? movie.overview.slice(0, 117) + '...'
                : movie.overview
            : 'No plot available.';

        card.innerHTML = `
            <div class="movie-poster">${poster}</div>
            <div class="movie-body">
                <h6>${movie.title}</h6>
                <p class="movie-plot" title="${movie.overview || ''}">${truncatedOverview}</p>
                <div>${movie.genres.map(g => `<span class="genre-badge">${g}</span>`).join('')}</div>
            </div>
        `;
        grid.appendChild(card);
    });
}


function showLoading() {
    document.getElementById('emptyState').style.display = 'none';
    document.getElementById('resultsArea').style.display = 'none';
    document.getElementById('loadingState').style.display = 'block';
}

// Scroll horizontally with arrows
function scrollHorizontally(id, amount) {
    document.getElementById(id).scrollBy({ left: amount, behavior: 'smooth' });
}

document.getElementById('getRecommendationsBtn').addEventListener('click', getRecommendations);
document.getElementById('surpriseMeBtn').addEventListener('click', getRecommendations);

renderMoods();
