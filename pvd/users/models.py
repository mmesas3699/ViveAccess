from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User."""

    pass
