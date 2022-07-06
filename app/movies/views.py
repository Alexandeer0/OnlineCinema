from django.shortcuts import render
from .models import Movie


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def player_page(request, kinopoisk_id):
    return render(request, 'movies/player.html', {'kinopoisk_id': kinopoisk_id})



def search(request, movie_name):
    #submitbutton = request.post.get("submit")
    #value

    movie_name=movie_name.lower().replace('%20',' ').replace('-',' ')
    movies = Movie.objects.all()
    for mv in movies:
        mv.lowername=mv.name.lower().replace('-',' ')
        mv.save()
    movies2=Movie.objects.filter(lowername__icontains=movie_name)
    if movies2.exists():
        return render(request, 'movies/index.html', {'movies': movies2})
    else:
        return render(request, 'movies/index.html', {'movies': movies})

