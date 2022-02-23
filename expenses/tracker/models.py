from datetime import datetime
from unicodedata import name
from django.db import models


# Create your models here.
class Expense(models.Model):
    """A class containing the info about an expense."""

    EXPENSES = (
        ('Groceries', 'Groceries'),
        ('Hygiene', 'Hygiene'),
        ('Makeup', 'Makeup'),
        ('Gifts', 'Gifts'),
        ('Cafe', 'Cafe'),
        ('Hobbies', 'Hobbies'),
        ('Restaurants', 'Restaurants'),
        ('Education', 'Education'),
        ('Other', 'Other'),
     )

    name: models.CharField = models.CharField(max_length=96, null=False, blank=True, unique=False)
    cost_dollars: models.DecimalField = models.DecimalField(max_digits=9, decimal_places=2)
    tag: models.CharField = models.CharField(max_length=50, null=True, blank=True, choices=EXPENSES)
    note: models.CharField = models.CharField(max_length=500, null=False, blank=True, unique=False)
    transaction_date: models.DateTimeField = models.DateTimeField(default=datetime.today, blank=False)

    def __str__(self) -> str:
        if self.name != '':
            return self.name
        return f'Expense({self.id})'