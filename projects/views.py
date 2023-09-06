from django.shortcuts import render
from .models import Project


# Create your views here.


# def list_projects(request):
#     projects = Project.objects.all()


#     return render(
#         request, "projects/list_projects.html", {"projects": projects}
#     )
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}

    return render(request, "projects/list_projects.html", context)
