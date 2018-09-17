from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')