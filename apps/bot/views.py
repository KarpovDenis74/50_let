from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from apps.bot.models import GroupBot
from apps.bot.forms import GroupBotForm


User = get_user_model()


@method_decorator(login_required, name='dispatch')
class GroupBotCreateView(CreateView):
    model = GroupBot
    form_class = GroupBotForm
    success_url = reverse_lazy('bot:bot_list')


@method_decorator(login_required, name='dispatch')
class GroupBotListView(ListView):
    model = GroupBot
    ordering = 'id'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class GroupBotDetailView(DetailView):
    model = GroupBot


@method_decorator(login_required, name='dispatch')
class GroupBotUpdateView(UpdateView):
    model = GroupBot
    form_class = GroupBotForm
    success_url = reverse_lazy('bot:bot_list')


@method_decorator(login_required, name='dispatch')
class GroupBotDeleteView(DeleteView):
    model = GroupBot
