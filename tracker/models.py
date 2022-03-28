from datetime import datetime
from django.db import models


# Create your models here.
class Expense(models.Model):
    """A class containing all the important info about an expense."""

    EXPENSES = (
        ("Groceries", "Groceries"),
        ("Hygiene", "Hygiene"),
        ("Makeup", "Makeup"),
        ("Gifts", "Gifts"),
        ("Cafe", "Cafe"),
        ("Hobbies", "Hobbies"),
        ("Restaurants", "Restaurants"),
        ("Education", "Education"),
        ("Other", "Other"),
    )

    cost_dollars: models.DecimalField = models.DecimalField(
        max_digits=9, decimal_places=2
    )
    tag: models.CharField = models.CharField(
        max_length=50, null=True, blank=True, choices=EXPENSES
    )
    note: models.CharField = models.CharField(
        max_length=500, null=False, blank=False, default="...", unique=False
    )
    transaction_date: models.DateTimeField = models.DateTimeField(
        default=datetime.today, blank=False
    )

    def __str__(self) -> str:
        """Return the string representation of the Expense object."""
        if self.note != "":
            return self.note
        return f"Expense({self.id})"
