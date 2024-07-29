from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import TemplateView

from apps.events.forms.forms import EventForm, EventGuestForm
from apps.events.models import Event, EventGuest, SamplePeriod


User = get_user_model()


@method_decorator(login_required, name='dispatch')
class EventView(TemplateView):
    template_name = 'events/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class EventListView(ListView):
    model = Event
    ordering = 'id'
    paginate_by = 1


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:events_list')


class GuestListView(ListView):
    model = EventGuest
    ordering = 'id'
    paginate_by = 1
    template_name = 'events/eventguest_list.html'

    def get_queryset(self):
        guest_list = EventGuest.objects.filter(event__pk=self.kwargs['event_pk'])
        return guest_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['event_pk'])
        return context

class GuestCreateView(CreateView):
    model = EventGuest
    form_class = EventGuestForm

    def get_success_url(self):
        pk = self.kwargs['event_pk']
        return reverse('events:guests_list', kwargs={"event_pk": pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['guest'].queryset = User.objects.exclude(eventguest__event=self.kwargs['event_pk'])
        return form

    def post(self, request, *args, **kwargs):
        self.event_pk = kwargs['event_pk']
        form = self.get_form()
        event = get_object_or_404(Event, pk=kwargs['event_pk'])
        form.instance.event_id = event.pk
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class GuestDeleteView(DeleteView):
    model = EventGuest

    def get_success_url(self):

        print(f'{self.object.event.pk}')
        return reverse('events:guests_list', kwargs={"event_pk": self.object.event.pk})

