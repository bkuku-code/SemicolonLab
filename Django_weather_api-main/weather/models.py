from django.db import models
from django.contrib.auth.models import AbstractUser


class WeatherUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=255)
    days = models.IntegerField(default=1)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # objects = MyAccountManager()

    def __str__(self):
        return self.location + '' + self.days
