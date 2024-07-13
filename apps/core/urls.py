from django.urls import path, include
from apps.core.views import index


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
]
