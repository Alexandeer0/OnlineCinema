from .views import index_page, player_page,search
from django.urls import path

urlpatterns = [
    path('', index_page),
    path('movie/<int:kinopoisk_id>', player_page),
    path('search/<str:movie_name>', search),
]
