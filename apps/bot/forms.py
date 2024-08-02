from django import forms
from django.contrib.auth import get_user_model

from apps.bot.models import GroupBot

User = get_user_model()


class GroupBotForm(forms.ModelForm):

    class Meta:
        model = GroupBot
        fields = ['name', 'description', 'token', 'group_id', 'active']