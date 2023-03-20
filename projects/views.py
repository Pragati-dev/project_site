from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    project = Project.objects.get()

    project_file = ProjectFile.objects.filter(project_name=project).first()

    context = {'file' : project_file.file }
    return render(request,'index.html',context)