from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def form(request):
    return render(request, 'forms/form.html', {})

def organization(request):
    form = ProjectRequestForm()
    if (request.method == 'POST'):
        form = ProjectRequestForm(request.POST)
        if (form.is_valid()):
            org = form.save(commit=False)
            org.save()

            return redirect('/')
    return render(request, 'contact.html', {'form': form})

def media(request):
    return render(request, 'form.html', {})

def school(request):
    return render(request, 'form.html', {})

def other(request):
    return render(request, 'form.html', {})