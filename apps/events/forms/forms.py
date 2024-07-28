from django import forms
from apps.events.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'place', 'start', 'stop', 'foto']
