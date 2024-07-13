from django.urls import path, include
from apps.events.views import EventsView



app_name = 'events'

urlpatterns = [
    path("", EventsView.as_view(), name="events"),
]
