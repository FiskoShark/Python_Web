from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #   ---   --- ролі користувачів #
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )

    # ---   ---   ---   ---   поле role #
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='user',
        verbose_name='Роль'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"



