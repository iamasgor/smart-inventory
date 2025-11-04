from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='user')

    def is_admin(self):
        return self.role == 'admin'
    def is_manager(self):
        return self.role == 'manager'