from django.contrib import admin
from .models import UserProfile
# Register your models here.
# admin.site.register(UserProfile)

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'password']


