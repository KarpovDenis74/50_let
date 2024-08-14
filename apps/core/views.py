from django.contrib.auth.views import LoginView
from apps.core.forms import NewAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView

User = get_user_model()


class NewLoginView(LoginView):
    form_class = NewAuthenticationForm


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('events:events_list')