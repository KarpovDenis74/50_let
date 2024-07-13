from apps.events.views import EventsView
from django.urls import path


app_name = 'events'

urlpatterns = [
    path("", EventsView.as_view(), name="events"),
]
