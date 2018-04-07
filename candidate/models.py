# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, help_text="Décris-toi rapidement ici.")
    location = models.CharField(max_length=30, blank=True, help_text="Où habites-tu ?")
    birth_date = models.DateField(null=True, blank=True, help_text="Utilise se format de date : <em>YYYY-MM-DD</em>.")

    items = models.ManyToManyField('Item', blank=True)
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return "Profile of {}; bio: {}; location: {}; birthday: {}.".format(
            self.user.username,
            self.bio,
            self.location,
            self.birth_date,
        )

class Item(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=10000, blank=True)  # need text area widget
    subitem = models.ManyToManyField('Subitem', blank=True)  # list
    # must delete also every subitems when deleting an item
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # TODO: null=True, on_delete=models.SET_NULL

    def __str__(self):
        msg = self.title
        if self.category:
            msg += ' in ' + self.category.name
        return msg

class Category(models.Model):
    name = models.CharField(max_length=25)
    item_related = models.BooleanField()  # True if it's a category for an item, else for a subitem
    # example: acvhievement, activity, project, contribution, hobby, voluntary work, set up, social (fb, lkd, tw...)

    #p.items.filter(category=c1)  get all item in a category

    def __str__(self):
        return self.name


class Subitem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=10000, blank=True)  # need text area widget
    category = models.ForeignKey('Category', on_delete=None, null=True, blank=True)

    def __str__(self):
        return self.title
