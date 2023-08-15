from django import forms
from .models import Ticket

class createTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'