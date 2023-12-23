from django.urls import path

from players import views


app_name = 'players'
players_urls = [
    path('hello/', views.hello, name='hello'),
]
