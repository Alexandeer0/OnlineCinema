from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse


def index_page(request):
    movies = Movie.objects.all()
    print(movies)
    return HttpResponse(300)

# def player_page(request, id):
#    return render(request, 'movies/player.html', {'id': id})
