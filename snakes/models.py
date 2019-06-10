from django.db import models
from .services import get_recent_caps

# Create your models here.
class Repo(models.Model):
    description = models.CharField(max_length=200, null=True)
    docs = models.CharField(max_length=200, null=True)
    github = models.CharField(max_length=200, null=True)
    gitter = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)

    def recent_caps():
        return get_recent_caps
