from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm


class NewAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()
