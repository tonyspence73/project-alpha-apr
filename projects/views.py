from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}

    return render(request, "projects/list_projects.html", context)
