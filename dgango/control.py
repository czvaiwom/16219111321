from . import getmovies,getphones,getweathers,view
import time
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
from django.shortcuts import render
from django.http import HttpResponse

def deletelall(request):
    context = {}
    try:
        Movies.objects.all().delete()
        Weathers.objects.all().delete()
        Phones.objects.all().delete()
        context['hello']='删除成功！'
    except:
        context['hello']='删除失败，请先写入数据！'
    return render(request, 'index.html', context)

def insertdata(request):
    context = {}
    try:
        getmovies.get_movies()
        time.sleep(2)
        getweathers.get_weather()
        time.sleep(2)
        getphones.get_phones('手机')        
        time.sleep(2)
        context['hello']='插入成功！'
    except:
        context['hello']='插入失败！'
    return render(request, 'index.html', context)

def updatabase(request):
    deletelall(request)
    insertdata(request)
    context = {}
    context['hello']='更新成功！'
    return render(request, 'index.html', context)
    
