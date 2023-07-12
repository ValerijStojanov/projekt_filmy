from django.shortcuts import render, HttpResponse
from filmy.data import filmy_data
# Create your views here.


def seznam(request):
    return render(request, 'filmy/seznam.html', context={'filmy_data': filmy_data})

def detail(request, slug):
    if slug in filmy_data:    
        film = filmy_data[slug]
        response = render(request, 'filmy/detail.html', context={'film': film})
        response['MOJE-DATA'] = 'Hello'
        # response['Content-Type'] = 'application/json; charset=utf-8' 
        return response
    else:
        raise HttpResponse('Film nebyl nalezen')