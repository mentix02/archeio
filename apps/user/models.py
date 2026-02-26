from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **extra_fields):

        if not email:
            raise ValueError(_('User must have an email address.'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password, **extra_fields):

        must_be_true_fields = ['is_staff', 'is_active', 'is_superuser', 'email_verified']

        for field in must_be_true_fields:
            extra_fields.setdefault(field, True)

            if not extra_fields.get(field):
                raise ValueError(_(f'Superuser must have {field}=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    objects = UserManager()

    username = None
    last_name = None
    first_name = None

    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=128, blank=True, db_default='')

    # Better-Auth core fields

    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField(blank=True, db_default='')
    email_verified = models.BooleanField(db_default=False)
    image = models.TextField(validators=[URLValidator()], blank=True, null=True, default=None)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def get_full_name(self) -> str:
        return self.name
