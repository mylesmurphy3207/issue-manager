from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.cascaade, null=True, blank=True)
    Role = models.ForeignKey(ROLE, on_delete=models.cascaade, null=True, blank=True)

# Create your models here.
