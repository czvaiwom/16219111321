from django.shortcuts import render
from django.http import HttpResponse
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
def index(request):
    context = {}
    context['hello']='Hello'
    return render(request, 'index.html', context)
 
def movies(request):
    movies=Movies.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def weathers(request):
    weathers=Weathers.objects.all()
    return render(request, 'weathers.html', {'weathers': weathers})

def phones(request):
    phones=Phones.objects.all()
    return render(request, 'phones.html', {'phones': phones})


    
