from apps.events.views import (EventDetailView, EventListView, EventCreateView,
                               GuestCreateView, GuestListView, GuestDeleteView,
                               SamplePeriodListView, SamplePeriodCreateView,
                               SamplePeriodDeleteView)

from django.urls import path


app_name = 'events'

urlpatterns = [
    path("events/<int:pk>/detail/", EventDetailView.as_view(),
         name="events_detail"),
    path("", EventListView.as_view(), name="events_list"),
    path("events/create/", EventCreateView.as_view(), name="events_create"),
    path("events/<int:event_pk>/guests/create/", GuestCreateView.as_view(),
         name="guests_create"),
    path("events/<int:event_pk>/guests/", GuestListView.as_view(),
         name="guests_list"),
    path("guests/<int:pk>/delete/", GuestDeleteView.as_view(),
         name="guests_delete"),
    path("events/<int:event_pk>/periods/", SamplePeriodListView.as_view(),
         name="periods_list"),
    path("events/<int:event_pk>/periods/create/",
         SamplePeriodCreateView.as_view(),
         name="periods_create"),
    path("period/<int:pk>/delete/", SamplePeriodDeleteView.as_view(),
         name="periods_delete"),
]
