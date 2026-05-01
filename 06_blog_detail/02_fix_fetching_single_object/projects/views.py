from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def detail(request, pk):
    # Utilise get_object_or_404 pour récupérer un seul objet
    # et retourner 404 si le projet n'existe pas
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
