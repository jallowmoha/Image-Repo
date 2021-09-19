from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.


class ManageUser(BaseUserManager):

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Password is required.')
        if email is None:
            raise TypeError('Email is required.')
        if username is None:
            raise TypeError('Username is required.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_user(self, username, email, password):
        if password is None:
            raise TypeError('Password is required.')
        if email is None:
            raise TypeError('Email is required.')
        if username is None:
            raise TypeError('Username is required.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = ManageUser()

    def __str__(self):
        return f"{self.email}"
