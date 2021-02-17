from django.contrib import admin
from profileApi import models

admin.site.register(models.ProfileFeedItem)
admin.site.register(models.UserProfile)
