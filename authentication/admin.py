from django.contrib import admin

# Register your models here.

from authentication.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']

