from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.all()
    ctx = {'projects': projects}
    return render(request, 'projects/projects.html', ctx)


def project(request, pk):
    project = Project.objects.get(id=pk)
    ctx = {'project': project}
    return render(request, 'projects/single-project.html', ctx)


def test(request):
    return HttpResponse('Test project route :)')
