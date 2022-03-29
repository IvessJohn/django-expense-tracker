"""Interface for sending forms via the website."""
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Expense


class ExpenseShortForm(ModelForm):
    """A form for adding expense logs via home page.
    Some Expense fields are omitted here.
    """

    class Meta:
        model = Expense
        fields = "__all__"
        # exclude = ['note', 'transaction_date']
        exclude = ["transaction_date"]


class ExpenseFullForm(ModelForm):
    """A form for adding expense logs via a dedicated expense add page.
    All Expense fields are included here.
    """

    class Meta:
        model = Expense
        fields = "__all__"
        exclude = []


class RegisterForm(UserCreationForm):
    """A custom form for user creation."""

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        exclude = []
