from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    Custom user model.
    As it is a AbstractUser, it has all the fields of the default User model Like:
    username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
    """

    last_active = models.DateTimeField(
        auto_now=True, help_text="Last time the user fulfilled the daily task"
    )
    streak_count = models.IntegerField(default=0, help_text="Current streak count")
    
    def __str__(self):
        return self.username
