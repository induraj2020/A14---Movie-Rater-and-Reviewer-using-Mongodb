from django.shortcuts import render
from .models import Movies
from .models import Comment, Rating
from .models import *
import random

# Create your views here.
from django.http import HttpResponse


def movie_list(request):
    moviess = Movies.objects.order_by('-imdbRating').all()
    print(moviess)
    return render(request, 'movies_list.html', {'moviess': moviess})

def movie_filter(request):
    moviess = Movies.objects.filter(title__icontains='Anand')
    return render(request, 'movies_list.html', {'moviess': moviess})

def movie_details(request, idMovie):
    movieTitle = Movies.objects.get(id=idMovie)
    moviess = Movies.objects.filter(title__icontains = movieTitle)
    # print(moviess)
    return render(request, 'movies_details.html', {'moviess': moviess})


def addComment(request, idMovie):
    if request.method == 'POST':
        newC = Comment()
        newC.commentT = request.POST['comment']

        newR = Rating()
        newR.ratingValue = request.POST['newRating']

        movie = Movies.objects.get(pk=idMovie)
        movie.comments.append(newC)
        movie.ratings.append(newR)
        movie.save()

    movieTitle = Movies.objects.get(id=idMovie)
    moviess = Movies.objects.filter(title__icontains=movieTitle)
    return render(request, 'movies_details.html', {'moviess': moviess})

def searching(request):
    moviess = Movies.objects.all()
    if request.method == 'GET':
        name_searched = request.GET.get('search_bar')
        year_gsearched=  request.GET.get('search_gyear')
        year_lsearched = request.GET.get('search_lyear')
        if (name_searched == None) and (year_gsearched == None) and(year_lsearched==None):
            moviess = Movies.objects.all()

        elif (request.GET.get('search_bar')):
            moviess = Movies.objects.filter(title__icontains=name_searched)

        elif(request.GET.get('search_gyear')):
            print(year_gsearched)
            moviess = Movies.objects.filter(year__gte=year_gsearched)

        elif (request.GET.get('search_lyear')):

            moviess = Movies.objects.filter(year__lt=year_lsearched)

    return render(request, 'searching.html', {'moviess': moviess})

def graphing(request):
    moviess = Movies.objects.all()
    T_movie_count = moviess.count()
    data_imdbraing=[]
    year_l =[]
    movie_count_by_year= []
    for element in moviess:
        data_imdbraing.append(element.imdbRating)
        year_l.append((int)(element.year))

    unqiue_year= list(set(year_l))

    for y in unqiue_year:
        movie_count_by_year.append(Movies.objects.filter(year=y).count())
    color_l=[]
    T_unique_count= len(unqiue_year)
    for i in range(len(unqiue_year)):
        color_l.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))

    context = {
        'movie_imdb_rating': data_imdbraing,
        'unqiue_year': unqiue_year,
        'movie_count_by_year': movie_count_by_year,
        'color_l': color_l,
        'T_movie_count':T_movie_count,
        'T_unique_count':T_unique_count

    }

    return render(request,'graphing.html',context)