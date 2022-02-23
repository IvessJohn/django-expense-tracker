from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    context = {

    }
    return render(request, 'tracker/dashboard.html', context)

def about(request):
    context = {

    }
    return render(request, 'tracker/about.html', context)