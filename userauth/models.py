from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE = (
    ("Doctor","Doctor"),
    ("Patient","Patient"),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(null=True, blank=True, max_length=255)
    user_type = models.CharField(max_length=50,choices=USER_TYPE , null=True , blank=True ,default=None)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.username or self.email  # Fallback to email if username is missing

    def save(self, *args, **kwargs):  # Corrected method name
        if not self.username:  # Check if username is empty or None
            email_username, _ = self.email.split("@")  # Split email to derive username
            self.username = email_username
        
        super(User, self).save(*args, **kwargs)  # Proper super call
