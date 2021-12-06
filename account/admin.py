from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        ('Information', {'fields': ('username', 'password', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    readonly_fields = ['date_joined',]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ['username']
    ordering = ['pk']

admin.site.register(User, CustomUserAdmin)

