from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("¡Hola, bienvenido a mi primera vista en Django!")  

def despedida(request):
    return HttpResponse("¡Adiós! ¡Gracias por visitar mi sitio web!")

def simple(request, name: str ):

    movies = [
        {'title': 'The Shawshank Redemption', 'year': 1994, 'director': 'Frank Darabont'},
        {'title': 'The Godfather', 'year': 1972, 'director': 'Francis Ford Coppola'},
        {'title': 'The Dark Knight', 'year': 2008, 'director': 'Christopher Nolan'},
        {'title': 'Pulp Fiction', 'year': 1994, 'director': 'Quentin Tarantino'},
        {'title': 'Forrest Gump', 'year': 1994, 'director': 'Robert Zemeckis'},
    ]

    return render(request, 'simple.html', {'nombre': name , 'movies': movies})

def simple2(request):
    return render(request, 'simple2.html')