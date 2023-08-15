from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    submitter = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name='project')
    def __str__(self):
        return self.name
