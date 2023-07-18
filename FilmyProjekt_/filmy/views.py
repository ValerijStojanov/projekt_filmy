from django.shortcuts import render, HttpResponse
from filmy.data import filmy_data
from django.http import JsonResponse
from django.utils.text import slugify
from filmy.data_herci import data_herci
# Create your views here.


def seznam(request):
    
    slug = slugify(request.GET.get("text", ""))
    
    if slug:
        data = {}
        for key_film in filmy_data:
            if key_film.startswith(slug):
                data[key_film] = filmy_data[key_film]
                
        context = {'filmy_data': data}
    else:
        context = {'filmy_data': filmy_data}
    
    return render(request, 'filmy/seznam.html', context=context)

def detail(request, slug):
    if slug in filmy_data:    
        film = filmy_data[slug]
        response = render(request, 'filmy/detail.html', context={'film': film})
        response['MOJE-DATA'] = 'Hello'
        # response['Content-Type'] = 'application/json; charset=utf-8' 
        return response
    else:
        raise HttpResponse('Film nebyl nalezen')
    
    
def seznam_json(request):
    return JsonResponse(filmy_data)

def seznam_hercu(request):
    return render(request, 'filmy/seznam_hercu.html', context={'data_herci': data_herci})

def detail_hercu(request, slug):
    herec = data_herci[slug]
    return render(request, 'filmy/detail_hercu.html', context={'herec': herec})