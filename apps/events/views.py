import asyncio

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView)

from apps.bot.models import GroupBot
from apps.events.forms import EventForm, EventGuestForm, SamplePeriodForm
from apps.events.models import Event, EventGuest, SamplePeriod
from apps.events.utils.foto import TUtils

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
        context['guests'] = (User.objects
                             .filter(eventguest__event=self.kwargs['pk']))
        return context


@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    model = Event
    ordering = 'id'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:events_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class GuestListView(TempGetContentData, ListView):
    model = EventGuest
    ordering = 'id'
    paginate_by = 20
    template_name = 'events/eventguest_list.html'

    def get_queryset(self):
        guest_list = (EventGuest.objects
                      .filter(event__pk=self.kwargs['event_pk']))
        return guest_list


@method_decorator(login_required, name='dispatch')
class GuestCreateView(TempPost, CreateView):
    model = EventGuest
    form_class = EventGuestForm

    def get_success_url(self):
        return reverse('events:guests_list',
                       kwargs={"event_pk": self.kwargs['event_pk']})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['guest'].queryset = (
            User.objects.exclude(eventguest__event=self.kwargs['event_pk'])
        )
        return form


@method_decorator(login_required, name='dispatch')
class GuestDeleteView(DeleteView):
    model = EventGuest

    def get_success_url(self):
        return reverse('events:guests_list',
                       kwargs={"event_pk": self.object.event.pk})


@method_decorator(login_required, name='dispatch')
class SamplePeriodListView(TempGetContentData, ListView):
    model = SamplePeriod
    ordering = 'id'
    paginate_by = 20

    def get_queryset(self):
        period_list = (
            SamplePeriod.objects.filter(event=self.kwargs['event_pk'])
        )
        return period_list


@method_decorator(login_required, name='dispatch')
class SamplePeriodCreateView(TempPost, TempGetContentData, CreateView):
    model = SamplePeriod
    form_class = SamplePeriodForm

    def get_success_url(self):
        return reverse('events:periods_list',
                       kwargs={"event_pk": self.kwargs['event_pk']})


@method_decorator(login_required, name='dispatch')
class SamplePeriodDeleteView(DeleteView):
    model = SamplePeriod

    def get_success_url(self):
        return reverse('events:periods_list',
                       kwargs={"event_pk": self.object.event.pk})


class FotoView(TemplateView):
    template_name = "events/event_foto_list.html"

    def _get_foto(self):
        bot = GroupBot.objects.get(pk=1)
        history = TUtils(bot)

        async def get_history():
            return await history.get_history()

        fotos = asyncio.run(get_history())
        # messages = history.get_history()
        # end_date = datetime.datetime.now()
        # start_date = end_date - datetime.timedelta(days=7)
        print(f'{fotos=}')
        return fotos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = self._get_foto()
        return context
