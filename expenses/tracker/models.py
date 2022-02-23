from datetime import datetime
from unicodedata import name
from django.db import models


# Create your models here.
class Expense(models.Model):
    """A class containing the info about an expense."""

    #region Transaction Types & Tags

    # TRANSACTION_TYPES = (('GAINS', 'GAINS'), ('EXPENSES', 'EXPENSES'))
# 
    # GAINS = (
        # ('Salary', 'Salary'),
        # ('Dividends', 'Dividends'),
        # ('Bonuses', 'Bonuses'),
        # ('Gifts', 'Gifts'),
        # ('Other', 'Other'),
    # )
    EXPENSES = (
        ('Groceries', 'Groceries'),
        ('Hygiene', 'Hygiene'),
        ('Makeup', 'Makeup'),
        ('Gifts', 'Gifts'),
        ('Cafe', 'Cafe'),
        ('Restaurants', 'Restaurants'),
        ('Education', 'Education'),
        ('Other', 'Other'),
     )
    # TAGS_CATEGORIES = {
        # 'GAINS': GAINS,
        # 'EXPENSES': EXPENSES
    # }

    #endregion

    name: models.CharField = models.CharField(max_length=96, null=False, blank=True, unique=False)
    cost_dollars: models.DecimalField = models.DecimalField(max_digits=9, decimal_places=3)
    # transaction_type: models.CharField = models.CharField(
                                                # max_length=50, null=True, 
                                                # choices=TRANSACTION_TYPES ) # expense/profit
    tag: models.CharField = models.CharField(max_length=50, null=True, blank=True, choices=EXPENSES)
    note: models.CharField = models.CharField(max_length=500, null=False, blank=True, unique=False)
    transaction_date: models.DateTimeField = models.DateTimeField(default=datetime.today, blank=False)
    date_created: models.DateTimeField = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        if self.name != '':
            return self.name
        return f'Expense_{self.id}'