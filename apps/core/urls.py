from django.urls import path, include
from apps.core.views import index
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path("", login_required(index), name="index"),
]
