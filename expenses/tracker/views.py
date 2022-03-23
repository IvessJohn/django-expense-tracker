"""Define all the views here."""
from calendar import month
from datetime import datetime
from django.http import QueryDict, HttpResponse
from django.shortcuts import render, redirect

from .models import Expense
from .forms import ExpenseFullForm, ExpenseShortForm

# Create your views here.
def dashboard(request):
    """The view of the main page."""
    expenses = Expense.objects.all().order_by("-transaction_date")
    
    # Expenses this year
    expenses_this_year = expenses.filter(
        transaction_date__date__year=datetime.now().year
    )
    total_this_year = sum(expense.cost_dollars for expense in expenses_this_year)
    # Expenses this month
    expenses_this_month = expenses.filter(
        transaction_date__date__month=datetime.now().month
    )
    total_this_month = sum(expense.cost_dollars for expense in expenses_this_month)

    expense_short_form: ExpenseShortForm = ExpenseShortForm()

    # Quick expense addition
    if request.method == "POST":
        expense_short_form = ExpenseShortForm(request.POST)
        if expense_short_form.is_valid():
            expense_short_form.save()
        return redirect("/")

    context = {
        "expenses": expenses,
        "expenses_this_year": expenses_this_year,
        "expenses_this_month": expenses_this_month,
        "expense_short_form": expense_short_form,
        "total_this_year": total_this_year,
        "total_this_month": total_this_month,
    }
    return render(request, "tracker/dashboard.html", context)


def about(request):
    """The view of the about page.
    Nothing interesting here.
    """
    context = {}
    return render(request, "tracker/about.html", context)


def add_expense_full_form(request):
    """A view for a full expense form, where the user can
    enter all the editable fields.
    """
    expense_full_form: ExpenseFullForm = ExpenseFullForm()

    if request.method == "POST":
        expense_full_form = ExpenseFullForm(request.POST)
        if expense_full_form.is_valid():
            expense_full_form.save()
        return redirect("/")

    context = {
        "expense_full_form": expense_full_form,
    }
    return render(request, "tracker/add_expense_full_form.html", context)


def expense_info(request, expense_id: int):
    """A view of an expense page. Here, the user can see and edit the information of
    the inspected expense.
    """
    expense: Expense = Expense.objects.get(id=expense_id)
    expense_full_form: ExpenseFullForm = ExpenseFullForm(instance=expense)

    # Update the expense
    if request.method == "POST":
        expense_full_form = ExpenseFullForm(request.POST, instance=expense)
        if expense_full_form.is_valid():
            expense_full_form.save()
        return redirect("/")

    context = {
        "expense": expense,
        "expense_full_form": expense_full_form,
    }
    return render(request, "tracker/expense_info.html", context)


def expense_delete(request, expense_id: int):
    """A view of an expense deletion confirmation page."""
    expense: Expense = Expense.objects.get(id=expense_id)

    # Remove the expense
    if request.method == "POST":
        expense.delete()
        return redirect("/")

    context = {
        "expense": expense,
    }
    return render(request, "tracker/expense_delete.html", context)
