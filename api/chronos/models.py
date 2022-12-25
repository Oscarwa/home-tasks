from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=250)
    # assigned_to = models.ForeignKey("api.User")
    due_date = models.DateField(default=None)
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
