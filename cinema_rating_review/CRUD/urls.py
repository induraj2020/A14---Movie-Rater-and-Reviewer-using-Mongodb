from django.contrib import admin
from . import views
from django.urls import re_path, include, path


urlpatterns = [
    path('', views.movie_list ,name='movie_list'),
    path('filter/', views.movie_filter ,name='movie_filter'),
    path('details/<int:idMovie>/', views.movie_details ,name='movie_details'),
    path('addComment/<int:idMovie>/', views.addComment ,name='addComment'),
    path('search/',views.searching, name='searching'),
    path('graphs/', views.graphing, name='graphing'),

]
