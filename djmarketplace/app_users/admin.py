from django.contrib import admin
from app_users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'balance', 'status']

admin.site.register(Profile, ProfileAdmin)
