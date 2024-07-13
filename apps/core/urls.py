from django.urls import path, include
from django.contrib.auth import views
from apps.core.views import index


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
]
