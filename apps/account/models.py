from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import MyUserManager

import uuid


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    activation_code = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def create_activation_code(self):
        code = str(uuid.uuid4())
        self.activation_code = code
    
    def __str__(self):
        return f'{self.email}'
    