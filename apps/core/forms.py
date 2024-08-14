from captcha.fields import CaptchaField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class NewAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone',
                  'avatar', 'middle_name', 't_nick')
