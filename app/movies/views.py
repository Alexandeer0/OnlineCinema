from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse

def index_page(request):
    return HttpResponse(1000)

def player_page(request, id):
    return render(request, 'movies/player.htmlm', {'id': id})
