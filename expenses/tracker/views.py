from django.shortcuts import render, redirect

from .models import Expense
# Create your views here.

def dashboard(request):
    expenses = Expense.objects.all()

    context = {
        'expenses': expenses,
    }
    return render(request, 'tracker/dashboard.html', context)

def about(request):
    context = {

    }
    return render(request, 'tracker/about.html', context)