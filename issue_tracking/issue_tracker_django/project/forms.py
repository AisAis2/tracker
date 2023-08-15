from django import forms
from .models import Project

class createProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','submitter']