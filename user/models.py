from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})

    def has_perm(self,perm,obj=None):
        if self.is_superuser:
            return True
        if obj is not None:
            return obj.author == self
        return False

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
