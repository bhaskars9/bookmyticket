from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    email = models.EmailField("Email Address",unique=True,max_length=255, blank=True, null=True)
    def __str__(self):
            return self.username