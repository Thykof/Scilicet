from django.contrib import admin

# Register your models here.

from candidate import models

admin.site.register(models.Profile)
