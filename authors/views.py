import random
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Author

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'authors/index.html', {
        'authors': Author.objects.all()
    })

def top_ten_authors(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()[:10]

    return render(request, 'authors/index.html', {
        'authors': authors
    })

def show(request: HttpRequest, author_id: int) -> HttpResponse:
    author = Author.objects.get(id=author_id)
    return HttpResponse(f"Author: {author.name} - Email: {author.email}")

def author_by_email(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.filter(email__icontains='example.com')

    return render(request, 'authors/index.html', {
        'authors': authors
    })



def author_by_age(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.filter(age__gte=30)

    return render(request, 'authors/index.html', {
        'authors': authors
    })

def turn_inactive(request: HttpRequest) -> HttpResponse:

    for number in range(20, 26):
        try:
            author = Author.objects.get(id=number)
            author.active = False
            author.save()
        except Author.DoesNotExist:
            continue

    return HttpResponse("Actualizar estados de autor a inactivo completado.")

def change_age(request: HttpRequest) -> HttpResponse:
    
    for author in Author.objects.all():
        author.age = random.randint(18, 56)
        author.save()

    return HttpResponse("Edades de autores actualizadas.")

def age_between(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.filter(age__gte=21, age__lte=30)

    return render(request, 'authors/index.html', {
        'authors': authors
    })