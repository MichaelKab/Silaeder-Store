from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)









