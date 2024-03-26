from django.db import models
from django.contrib.auth.models import User




class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    assignees = models.ManyToManyField(User)
    submitter = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name='created_project')
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
