
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.signing import Signer
from django.db import models
import uuid
import datetime
from pathlib import Path


def images_avatar_path(instance, filename):
    """
        функция возвращает директорию для загрузки логотипа
        в модель Company
    """
    _date = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')
    filename = _date + '.' + str(filename.split('.')[-1])

    filename = str(instance.username) + '-' + filename
    path = Path('avatars/') / Path(filename)

    return str(path)


class CustomUserManager(UserManager):
    """
        Переопределим логику сохранения пользователей
    """
    def _create_user(self, username, email, password, **extra_fields):
        print('_create_user     ')
        signer = Signer()
        signer_password = signer.sign_object({'password': password})
        print(f'{signer_password=}')
        extra_fields.setdefault('signer_password', signer_password)
        return super()._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    confirmation_code = models.CharField(
        max_length=255, editable=True, blank=True,
        unique=True, verbose_name='Код подтверждения email')
    phone = models.CharField(max_length=25, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    t_nick = models.CharField(max_length=150, blank=True,
                              verbose_name='Telegram nickname')
    t_id = models.CharField(max_length=150, blank=True,
                            verbose_name='Telegram id')
    foto = models.ImageField(upload_to='users/foto/', blank=True)
    signer_password = models.TextField(blank=True, verbose_name='Хэш пароля')
    objects = CustomUserManager()
    avatar = models.ImageField(upload_to=images_avatar_path, blank=True,
                               default='avatars/default.webp')

    def __str__(self):
        return f'{self.username}: {self.full_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def password_from_hash(self):
        """
            Возвращает пароль из поля хэша
        """
        signer = Signer()
        raw_password = signer.unsign_object(self.signer_password)
        try:
            data_dict = eval(str(raw_password))
            data = data_dict.get('password')
        except Exception:
            data_dict = ''
        return data

    def set_password(self, raw_password):
        """
            Создает хэш пароля из raw_password
            и сохраняет его в поля hash_password
            и password
        """
        signer = Signer()
        self.signer_password = signer.sign(raw_password)

        # устанавливает mda5 хэш пароля
        self.password = make_password(raw_password)
        self._password = raw_password

    def save(
        self, force_insert=False, force_update=False, using=None,
        update_fields=None
    ):
        print('Метод save()')
        self.confirmation_code = uuid.uuid4()
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-pk']
