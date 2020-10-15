from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    # 'null=True': allows storing a database entry as null
    # 'blank=True': allows empty values on forms
    age = models.PositiveIntegerField(null=True, blank=True)
