from django.urls import path

from apps.bot.views import (GroupBotCreateView, GroupBotDeleteView,
                            GroupBotDetailView, GroupBotListView,
                            GroupBotUpdateView)

app_name = 'bot'

urlpatterns = [
    path("<int:pk>/detail/", GroupBotDetailView.as_view(),
         name="bot_detail"),
    path("create/", GroupBotCreateView.as_view(), name="bot_create"),
    path("<int:pk>/delete/", GroupBotDeleteView.as_view(), name="bot_delete"),
    path("<int:pk>/update/", GroupBotUpdateView.as_view(), name="bot_update"),
    path("", GroupBotListView.as_view(), name="bot_list"),
]