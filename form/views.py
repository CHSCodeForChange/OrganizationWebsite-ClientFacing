from django.shortcuts import render, redirect

# Create your views here.
def form(request):
    return render(request, 'form.html', {})
