from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Viviana Arango'})

def about(request):
    return HttpResponse('<h1>This is an About Page</h1>')
