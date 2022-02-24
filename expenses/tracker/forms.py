"""Interface for sending forms via the website."""
from django import forms
from django.forms import ModelForm

from .models import Expense


class ExpenseShortForm(ModelForm):
    """A form for adding expense logs via home page.
    Some Expense fields are omitted here.
    """
    class Meta:
        model = Expense
        fields = '__all__'
        #exclude = ['note', 'transaction_date']
        exclude = ['transaction_date']

class ExpenseFullForm(ModelForm):
    """A form for adding expense logs via a dedicated expense add page.
    All Expense fields are included here.
    """
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = []