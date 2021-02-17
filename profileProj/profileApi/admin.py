from django.contrib import admin
from profileProj.profileApi import models

admin.site.register(models.ProfileFeedItem)
admin.site.register(models.UserProfile)
