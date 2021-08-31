from djongo import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name="", last_name=""):
        if email is None:
            raise TypeError("Users should have email")

        user = self.model(email=self.normalize_email(
            email), password=password, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError("Password should not None")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    PROVIDER = (
        ("default", "default"),
        ("Google", "Google"),
    )
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    provider = models.CharField(
        max_length=20, choices=PROVIDER, default=PROVIDER[0][0])
    first_name = models.CharField(
        max_length=20, default="")
    last_name = models.CharField(
        max_length=20, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    def token(self):
        token = RefreshToken.for_user(self)
        return {
            "access_token": str(token.access_token),
            "refresh": str(token),
            "data": self.to_dict()
        }

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "provdier": self.provider
        }
