from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models. EmailField(unique=True)
    username = models.CharField(null=True, blank=True,max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def __save__(self, *args, **kwargs):
        email_username, _ = self.email.split("@")  # desphixs @ gmail.com
        if self.username == "" or self.username == None:
            self.username = email_username

            super(User, self).save(*args, **kwargs)
