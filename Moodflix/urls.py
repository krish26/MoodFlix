from django.contrib import admin
from django.urls import path,include
from Moodflix import views


urlpatterns = [
    path('', views.index, name='index'),
    path('moods/', views.get_moods, name='get_moods'),
    path('recommendations/', views.get_recommendations, name='get_recommendations'),
    #path('surprise/', views.get_surprise_recommendations, name='get_surprise'),
    #path('similar/', views.get_similar_movies, name='get_similar'),
    #path('mixed-mood/', views.get_mixed_mood_recommendations, name='get_mixed_mood'),
    #path('search/', views.search_movies, name='search_movies'),
]