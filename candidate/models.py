# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=25)
    email_address = models.EmailField()
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Profile of {}; bio: {}; location: {}; birthday: {}.".format(
            self.user.username,
            self.bio,
            self.location,
            self.birth_date,
        )

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
