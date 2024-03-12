from django.http import HttpResponse

def saludo(request):
  return HttpResponse('hi djcadaniel')

def despedida(request):
  return HttpResponse('by djcadaniel')

def adulto(request, edad):
  if edad >= 18:
    return HttpResponse("eres mayor de edad")
  else:
    return HttpResponse("No eres mayor de edad")