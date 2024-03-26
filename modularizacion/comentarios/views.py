from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
  return HttpResponse("Funciona correctamente")

def create(request):
  # comment = Comment(name='djcadaniel', score=5, comment='Esta es una prueba')
  # comment.save()
  comment = Comment.objects.create(name='djcadaniel')
  return HttpResponse('Ruta para probar la creación de modelos')

def delete(request):
  # comment = Comment.objects.get(id=1)
  # comment.delete()
  Comment.objects.filter(id=2).delete()
  return HttpResponse('Ruta para probarlos borrados')