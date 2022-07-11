from django.shortcuts import render
from .models import Movie
from .forms import MovieForm


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def player_page(request, kinopoisk_id):
    movies = Movie.objects.filter(kinopoisk_id=kinopoisk_id)
    for movie in movies:
        return render(request, 'movies/player.html', {'movie': movie})




def search(request):
    #submitbutton = request.POST.get("submit")
    form = MovieForm(request.POST)
    moviename=""
    if form.is_valid():
        moviename = form.cleaned_data.get("moviename")

    moviename=moviename.lower().replace('%20',' ').replace('-',' ')
    movies = Movie.objects.all()
    for mv in movies:
        mv.lowername=mv.name.lower().replace('-',' ')
        mv.save()
    movies2=Movie.objects.filter(lowername__icontains=moviename)
    if movies2.exists():
        return render(request, 'movies/index.html', {'movies': movies2})
    else:
        return render(request, 'movies/index.html', {'movies': movies})
