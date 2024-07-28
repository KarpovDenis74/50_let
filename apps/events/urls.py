from apps.events.views import EventView, EventListView, EventCreateView
from django.urls import path


app_name = 'events'

urlpatterns = [
    path("", EventView.as_view(), name="events"),
    path("events_list/", EventListView.as_view(), name="events_list"),
    path("events_create/", EventCreateView.as_view(), name="events_create"),
]
