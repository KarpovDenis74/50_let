from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from apps.core.views import NewLoginView, UserCreateView


urlpatterns = [
    path("bot/", include("apps.bot.urls")),
    path("core/", include("apps.core.urls")),
    path("", include("apps.events.urls")),
    path("admin/", admin.site.urls),
    path("accounts/login/", NewLoginView.as_view(), name="login"),
    path('accounts/registration/',
         UserCreateView.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
