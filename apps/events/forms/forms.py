from django import forms
from apps.events.models import Event, EventGuest, SamplePeriod
from django.contrib.auth import get_user_model


User = get_user_model()

class EventForm(forms.ModelForm):
    start = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Начало события',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'datetime-local',}),
    )
    stop = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Окончание события',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Event
        fields = ['name', 'description', 'place', 'start', 'stop', 'foto']


class EventGuestForm(forms.ModelForm):

    class Meta:
        model = EventGuest
        fields = ['guest']


class SamplePeriodForm(forms.ModelForm):
    t_start = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Начало выборки',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'datetime-local',}),
    )
    t_stop = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Окончание выборки',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = SamplePeriod
        fields = ['t_start', 't_stop']