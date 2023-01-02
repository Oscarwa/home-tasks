from django.db import models


class GroceryLevel(models.TextChoices):
    EMPTY = ("empty",)
    LOW = ("low",)
    NORMAL = ("normal",)
    FULL = "full"


class Grocery(models.Model):
    name = models.CharField(max_length=120)
    level = models.CharField(
        max_length=20, choices=GroceryLevel.choices, default=GroceryLevel.EMPTY
    )
    updated_at = models.DateTimeField(auto_now=True)
    home = models.ForeignKey("home.Home", on_delete=models.CASCADE)
