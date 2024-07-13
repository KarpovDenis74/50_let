from django.shortcuts import render
from django.views.generic.base import TemplateView


class EventsView(TemplateView):
    template_name = 'events/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
