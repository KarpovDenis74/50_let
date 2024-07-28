from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView
from apps.events.models import Event
from apps.events.forms.forms import EventForm


@method_decorator(login_required, name='dispatch')
class EventView(TemplateView):
    template_name = 'events/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class EventListView(ListView):
    model = Event
    ordering = 'id'


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:list')
