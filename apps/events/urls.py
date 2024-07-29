from apps.events.views import (EventView, EventListView, EventCreateView,
                               GuestCreateView, GuestListView, GuestDeleteView)

from django.urls import path


app_name = 'events'

urlpatterns = [
    path("detail/<int:event_pk>/", EventView.as_view(), name="event_detail"),
    path("events-list/", EventListView.as_view(), name="events_list"),
    path("events-create/", EventCreateView.as_view(), name="events_create"),
    path("guests-create/<int:event_pk>/", GuestCreateView.as_view(), name="guests_create"),
    path("guests-list/<int:event_pk>/", GuestListView.as_view(), name="guests_list"),
    path("guests-delete/<int:pk>/", GuestDeleteView.as_view(), name="guests_delete"),
]
