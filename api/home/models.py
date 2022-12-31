from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class MemberManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.name = name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, name, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    home = models.ForeignKey("home.Home", on_delete=models.CASCADE)

    email = models.CharField(max_length=255, unique=True, default="test@home-task.com")
    password = models.CharField(max_length=255, default="123qwe")
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    objects = MemberManager()

    def __str__(self):
        return f"{self.name} - {self.email} @ {self.home}"


class Home(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    admin = models.ForeignKey(
        Member, on_delete=models.DO_NOTHING, related_name="home_admin"
    )

    def __str__(self):
        return self.name
