from django.contrib import admin
from .models import Movie, UserPreference


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'vote_average', 'vote_count', 'release_date']
    list_filter = ['release_date']
    search_fields = ['title', 'overview']
    ordering = ['-vote_average']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('tmdb_id', 'title', 'overview', 'release_date', 'runtime')
        }),
        ('Ratings & Popularity', {
            'fields': ('vote_average', 'vote_count', 'popularity')
        }),
        ('Media', {
            'fields': ('poster_path',)
        }),
        ('Cast & Crew', {
            'fields': ('genres', 'cast', 'director')
        }),
        ('Mood Scores', {
            'fields': (
                'mood_happy', 'mood_sad', 'mood_excited', 'mood_scared',
                'mood_romantic', 'mood_thoughtful', 'mood_adventurous',
                'mood_relaxed', 'mood_mysterious', 'mood_inspired'
            ),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'created_at', 'updated_at']
    search_fields = ['session_key']
    ordering = ['-updated_at']
