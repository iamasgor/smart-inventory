from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_short_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_name