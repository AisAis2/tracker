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
    assignees = UserSerializer(allow_null=True,many=True)
    submitter = UserSerializer(allow_null=True)
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "submitter",
            'assignees'
        )
    def create(self,data):
        submitter=None
        if 'submitter' in data and data['submitter']!=None:
            submitter_data = data.pop('submitter')
            submitter = User.objects.get(username=submitter_data['username'])
        if 'assignees' in data:
            assignees_data =data.pop('assignees')
        project = Project.objects.create(**data)
        if submitter!=None:
            project.submitter=submitter
            project.save()
        return project
    def update(self,instance,validated_data):
        if 'assignees' in validated_data:
            assignees_data = validated_data.pop('assignees')
        if 'submitter' in validated_data and validated_data['submitter']!=None:
            submitter_data= validated_data.pop('submitter')
            instance.submitter = User.objects.get(username=submitter_data['username'])
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        for i in assignees_data:
            u=User.objects.get(username=i['username'])
            instance.assignees.add(u)
        instance.save()
        return instance
        
