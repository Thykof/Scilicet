# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    items = models.ManyToManyField('Item')

    def __str__(self):
        return "Profile of {}; bio: {}; location: {}; birthday: {}.".format(
            self.user.username,
            self.bio,
            self.location,
            self.birth_date,
        )

class Item(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=10000, null=True)  # need text area widget
    subitem = models.ManyToManyField('Subitem')  # list
    # must delete also every subitems when deleting an item
    category = models.ForeignKey('Category', on_delete=None, null=True)  # TODO: null=True, on_delete=models.SET_NULL

class Category(models.Model):
    name = models.CharField(max_length=25)
    item_related = models.BooleanField()  # True if it's a category for an item, else for a subitem
    # example: acvhievement, activity, project, contribution, hobby, voluntary work, set up, social (fb, lkd, tw...)

    def __str__(self):
        return self.name


class Subitem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)  # need text area widget
    category = models.ForeignKey('Category', on_delete=None, null=True)

    def __str__(self):
        return self.title
