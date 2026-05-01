from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def detail(request, pk):
    # Récupère le projet avec l'ID passé en paramètre
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})