from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField


from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField


class Movie(models.Model):
    """Movie model to store movie data in SQLite"""
    
    tmdb_id = models.IntegerField(unique=True, db_index=True)
    title = models.CharField(max_length=500)
    overview = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    
    vote_average = models.FloatField(db_index=True)
    vote_count = models.IntegerField()
    popularity = models.FloatField()
    
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    
    # Store genres and cast as JSON
    genres = JSONField(default=list)  # List of genre names
    cast = JSONField(default=list)    # List of actor names
    director = models.CharField(max_length=200, null=True, blank=True)
    
    # Mood scores
    mood_happy = models.FloatField(default=0, db_index=True)
    mood_sad = models.FloatField(default=0, db_index=True)
    mood_excited = models.FloatField(default=0, db_index=True)
    mood_scared = models.FloatField(default=0, db_index=True)
    mood_romantic = models.FloatField(default=0, db_index=True)
    mood_thoughtful = models.FloatField(default=0, db_index=True)
    mood_adventurous = models.FloatField(default=0, db_index=True)
    mood_relaxed = models.FloatField(default=0, db_index=True)
    mood_mysterious = models.FloatField(default=0, db_index=True)
    mood_inspired = models.FloatField(default=0, db_index=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-vote_average', '-vote_count']
        indexes = [
            models.Index(fields=['vote_average', 'vote_count']),
            models.Index(fields=['popularity']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_mood_score(self, mood):
        """Get mood score for a specific mood"""
        return getattr(self, f'mood_{mood}', 0)


class UserPreference(models.Model):
    """Store user preferences and history (optional, for future enhancement)"""
    
    session_key = models.CharField(max_length=40, db_index=True)
    favorite_genres = JSONField(default=list)
    excluded_genres = JSONField(default=list)
    viewed_movies = JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Preferences for {self.session_key}"



