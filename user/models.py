from django.db import models
from django.contrib.auth.models import AbstractUser


# class UserModel(models.Model):
#     class Meta:
#             db_table = "user"
#
#     name = models.CharField(max_length=20, null=False)
#     gender = models.CharField(max_length=10, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class UserModel(AbstractUser):
    class Meta:
            db_table = "user"

    name = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
