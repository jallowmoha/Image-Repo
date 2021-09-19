from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username')
    ordering = ['date_created']
    list_display = ('email', 'username', 'is_active', 'is_staff')


admin.site.register(User, UserAdminConfig)

# Register your models here.
