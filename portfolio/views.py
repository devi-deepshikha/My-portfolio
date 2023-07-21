from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')



def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/myprojects.html',{'projects':projects})
