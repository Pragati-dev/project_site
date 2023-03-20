from django.contrib import admin
from .models import Project,Category,ProjectFile
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','title']

admin.site.register(Project, ProjectAdmin)

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['project_name','file']

admin.site.register(ProjectFile, ProjectFileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)