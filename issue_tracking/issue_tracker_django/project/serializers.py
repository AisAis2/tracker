from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
        extra_kwargs = {
            'username':{
                'validators':[UnicodeUsernameValidator()],
            }
        }
class ProjectSerializer(serializers.ModelSerializer):
    submitter = UserSerializer(allow_null=True)
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "submitter"
        )
    def create(self,data):
        submitter=None
        if 'submitter' in data and data['submitter']!=None:
            submitter_data = data.pop('submitter')
            submitter = User.objects.get(username=submitter_data['username'])
        project = Project.objects.create(**data)
        if submitter!=None:
            project.submitter=submitter
            project.save()
        return project