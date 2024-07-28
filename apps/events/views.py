from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


@method_decorator(login_required, name='dispatch')
class EventsView(TemplateView):
    template_name = 'events/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
