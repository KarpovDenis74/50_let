from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.views.generic.base import TemplateView

from apps.events.forms.forms import EventForm, EventGuestForm, SamplePeriodForm
from apps.events.models import Event, EventGuest, SamplePeriod


User = get_user_model()


class TempGetContentData():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['event_pk'])
        return context


class TempPost():
    def post(self, request, *args, **kwargs):
        self.event_pk = kwargs['event_pk']
        form = self.get_form()
        event = get_object_or_404(Event, pk=kwargs['event_pk'])
        form.instance.event_id = event.pk
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guests'] = User.objects.filter(eventguest__event=self.kwargs['pk'])
        return context


class EventListView(ListView):
    model = Event
    ordering = 'id'
    paginate_by = 5


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:events_list')


class GuestListView(TempGetContentData, ListView):
    model = EventGuest
    ordering = 'id'
    paginate_by = 20
    template_name = 'events/eventguest_list.html'

    def get_queryset(self):
        guest_list = EventGuest.objects.filter(event__pk=self.kwargs['event_pk'])
        return guest_list


class GuestCreateView(TempPost, CreateView):
    model = EventGuest
    form_class = EventGuestForm

    def get_success_url(self):
        return reverse('events:guests_list',
                       kwargs={"event_pk": self.kwargs['event_pk']})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['guest'].queryset = User.objects.exclude(eventguest__event=self.kwargs['event_pk'])
        return form


class GuestDeleteView(DeleteView):
    model = EventGuest

    def get_success_url(self):
        return reverse('events:guests_list',
                       kwargs={"event_pk": self.object.event.pk})


class SamplePeriodListView(TempGetContentData, ListView):
    model = SamplePeriod
    ordering = 'id'
    paginate_by = 20

    def get_queryset(self):
        period_list = SamplePeriod.objects.filter(event=self.kwargs['event_pk'])
        return period_list


class SamplePeriodCreateView(TempPost, TempGetContentData, CreateView):
    model = SamplePeriod
    form_class = SamplePeriodForm

    def get_success_url(self):
        return reverse('events:periods_list',
                       kwargs={"event_pk": self.kwargs['event_pk']})


class SamplePeriodDeleteView(DeleteView):
    model = SamplePeriod

    def get_success_url(self):
        return reverse('events:periods_list',
                       kwargs={"event_pk": self.object.event.pk})