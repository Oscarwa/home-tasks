from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=250)
    assigned_to = models.ForeignKey("home.Member", on_delete=models.CASCADE)
    home = models.ForeignKey("home.Home", on_delete=models.CASCADE)
    due_date = models.DateField(default=None)
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
