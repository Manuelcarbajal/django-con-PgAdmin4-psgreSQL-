from django.shortcuts import render
# from django.http import HttpResponse
from .models import Curso

# def home(request):
#     return HttpResponse("<h1>Hola como estas</h1>")


def home(request):
    cursoList=Curso.objects.all()
    return render(request,"gestioncursos.html",{"cursos":cursoList})
