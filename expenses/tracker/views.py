from typing import List
from django.http import QueryDict
from django.shortcuts import render, redirect

from .models import Expense
from .forms import ExpenseFullForm, ExpenseShortForm
# Create your views here.

def dashboard(request):
    expenses = Expense.objects.all()
    expense_short_form: ExpenseShortForm = ExpenseShortForm()

    # Shorthand expense addition
    if request.method == "post":
        expense_short_form = ExpenseFullForm(request.post)
        if expense_short_form.is_valid():
            expense_short_form.save()
        return redirect('/')

    context = {
        'expenses': expenses,
        'expense_short_form': expense_short_form,
    }
    return render(request, 'tracker/dashboard.html', context)

def about(request):
    context = {

    }
    return render(request, 'tracker/about.html', context)

def expense_info(request, expense_id: int):
    expense: Expense = Expense.objects.get(id=expense_id)
    expense_full_form: ExpenseFullForm  = ExpenseFullForm(instance=expense)

    # Update the expense
    if request.method == "post_update":
        expense_full_form = ExpenseFullForm(request.post, instance=expense)
        if expense_full_form.is_valid():
            expense_full_form.save()
        return redirect('expense/<str:expense_id>/')
    # Remove the expense
    if request.method == "post_remove":
        expense.delete()
        return redirect('/')

    context = {
        'expense': expense,
        'expense_full_form': expense_full_form,
    }
    return render(request, 'tracker/expense_info.html', context)

def add_expense_full_form(request):
    expense_full_form: ExpenseFullForm = ExpenseFullForm()

    if request.method == "post":
        expense_full_form = ExpenseFullForm(request.post)
        if expense_full_form.is_valid():
            expense_full_form.save()

    context = {
        'expense_full_form': expense_full_form,
    }
    return render(request, 'tracker/add_expense_full_form.html', context)