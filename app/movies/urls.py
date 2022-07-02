from .views import index_page, player_page
from django.urls import path

urlpatterns = [
    path('', index_page),
    path('movie/<int:kinopoisk_id>', player_page),
]
