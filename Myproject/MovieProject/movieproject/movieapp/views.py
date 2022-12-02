from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForm


# Create your views here.

def index(requests):
    movies = Movies.objects.all()
    context ={
        'movies_list':movies
    }
    return render(requests, 'index.html',context)


def detail(requests, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(requests,'detail.html',{'movie':movie})

def add_movies(requests):
    if requests.method == "POST":
        name=requests.POST['name']
        desc=requests.POST['desc']
        year=requests.POST['year']
        img=requests.FILES['img']
        movies= Movies(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(requests,'add.html')

def update(requests, movie_id):
    movie = Movies.objects.get(id=movie_id)
    form = MovieForm(requests.POST or None, requests.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    data = {
        'movie_info':movie
    }
    return render(requests,'update.html',{'form':form,'movie':movie})

def delete(requests, id):
    if requests.method == "POST":
        movie= Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(requests,'delete.html')