from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Meta:
        ordering = ['pk']
    username = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(max_length = 130, unique = True, null = False)
    phone_number = models.CharField(max_length = 13, null = True, blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f"{self.username} - {self.email}"