from django.contrib.auth.views import LoginView
from apps.core.forms import NewAuthenticationForm


class NewLoginView(LoginView):
    form_class = NewAuthenticationForm
