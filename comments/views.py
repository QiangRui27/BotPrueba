from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.

def create(request)-> HttpResponse:
    #comment = Comment(name = 'Comentario 1', score=5, comment='Este es el primer comentario')
    #comment.save()

    Comment.objects.create(name='Comentario2', score=5, comment='Este es el segundo comentario')

    return HttpResponse("Comment created successfully!")

def delete(request) -> HttpResponse:

    #comment_to_delete = Comment.objects.get(id=1)
    #comment_to_delete.delete()
    Comment.objects.filter(id=2).delete()

    return HttpResponse("Comment deleted successfully!")