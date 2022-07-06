from django.contrib import admin

from poll.models import Poll, Profile


# Register your models here.
admin.site.register(Poll)
admin.site.register(Profile)