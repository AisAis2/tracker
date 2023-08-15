from rest_framework import serializers
from .models import Project
# from project.models import TicketSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "submitter"
        )
    