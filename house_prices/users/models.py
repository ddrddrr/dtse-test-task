from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("The `email` field is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs["is_admin"] = True
        kwargs["is_superuser"] = True
        return self.create_user(email=email, password=password, **kwargs)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    objects = UserManager()
