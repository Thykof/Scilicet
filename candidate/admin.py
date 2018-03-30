from django.contrib import admin

# Register your models here.

from candidate import models

admin.site.register(models.Profile)
admin.site.register(models.Item)
admin.site.register(models.Achievement)
admin.site.register(models.Project)
