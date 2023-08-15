from rest_framework import serializers
from .models import Ticket
from project.serializers import ProjectSerializer
from project.models import Project
from .forms import createTicket

class TicketSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False,allow_null= True)
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
        print(data)
        if 'project' in data and data['project']!=None:
            project_data = data.pop('project')
            project = Project.objects.get(name = project_data['name'])
        t = Ticket.objects.create(**data)
        if project!=None:
            t.project= project
            t.save()
        return t
    def update(self,instance,validated_data):
        print(validated_data)
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