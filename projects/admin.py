from django.contrib import admin
from projects.models import Project

# Register your models here.
admin.site.register(Project)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
        "id",
    )
