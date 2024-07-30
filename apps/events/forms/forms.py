from django import forms
from apps.events.models import Event, EventGuest, SamplePeriod
from django.contrib.auth import get_user_model


User = get_user_model()

class EventForm(forms.ModelForm):
    start = forms.DateField(
        label='Начало события',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date',}),
    )
    stop = forms.DateField(
        label='Окончание события',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Event
        fields = ['name', 'description', 'place', 'start', 'stop', 'foto']


class EventGuestForm(forms.ModelForm):

    class Meta:
        model = EventGuest
        fields = ['guest']


class SamplePeriodForm(forms.ModelForm):
    t_start = forms.DateField(
        label='Начало выборки',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date',}),
    )
    t_stop = forms.DateField(
        label='Окончание выборки',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = SamplePeriod
        fields = ['t_start', 't_stop']