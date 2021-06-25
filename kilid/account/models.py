import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import *
from django.db.models.deletion import CASCADE
from django.utils.functional import empty
from django.utils.translation import gettext_lazy as _
import datetime




class CustomAccountManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self, user_name, password=None):
        """Creates and saves a User with the given user_name and password."""
        if not user_name:
            raise ValueError('Users must have user_name number')
        user = self.model(
            user_name=user_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password):
        """Creates and saves a superuser with the given user_name and password."""
        user = self.create_user(user_name=user_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()
    user_name = models.CharField(
        _('username'),
        validators=[username_validator],
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    my_file = models.FileField(upload_to='upload/', blank=True)
    size = models.FloatField(blank=True ,default=0)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    my_name= models.CharField(max_length=150,blank=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.user_name
