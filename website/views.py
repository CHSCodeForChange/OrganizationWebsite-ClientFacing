from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})
def projects(request):
    return render(request, 'projects.html', {})
def team(request):
    return render(request, 'team.html', {})
def map(request):
    return render(request, 'map.html', {})
