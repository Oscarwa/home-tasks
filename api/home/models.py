from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Home(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    admin = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
