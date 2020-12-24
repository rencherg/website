from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home/index.html')
    return render(request, 'home/index.html')

def gallery(request):
    template = loader.get_template('home/gallery.html')
    return render(request, 'home/gallery.html')

def about(request):
    template = loader.get_template('home/about.html')
    return render(request, 'home/about.html')
