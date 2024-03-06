from rest_framework import serializers
from .models import Ticket
from project.serializers import ProjectSerializer
from project.models import Project
from .forms import createTicket
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
class TicketSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False,allow_null= True)
    submitter = UserSerializer(allow_null=True)
    class Meta:
        model = Ticket
        fields = (
            'id',
            'title',
            'description',
            'submitter',
            'assigned',
            'project',
            'status',
            'type',
            'priority',
        )
    def create(self, data):
        project=None
        user=None
        if 'project' in data and data['project']!=None:
            project_data = data.pop('project')
            project = Project.objects.get(name = project_data['name'])
        if 'submitter' in data and data['submitter']!=None:#not saving user
            user_data=data.pop('submitter')
            user =  User.objects.get(username=user_data['username'])
        t = Ticket.objects.create(**data)
        if project!=None:
            t.project= project
            t.save()
        if user!=None:
            t.submitter=user
            t.save()

        return t
    def update(self,instance,validated_data):
        if 'project' in validated_data and validated_data['project']!=None:
            project_data = validated_data.pop('project')
            instance.project = Project.objects.get(name = project_data['name'])
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.status = validated_data.get('status',instance.status)
        instance.priority = validated_data.get('priority',instance.priority)
        instance.type = validated_data.get('type',instance.type)
        instance.save()
        return instance