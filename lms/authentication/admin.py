from django.contrib import admin
from .models import User, Professor, HOD
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdminConfig(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "user_name", "first_name",
                    'user_type', 'is_verified')

    fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name')
        }),

        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )
    add_fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2')
        }),

        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )


@admin.register(Professor)
class ProfessorAdminConfig(UserAdmin):
    ordering = ("email",)
    list_display = ('id', "email", "user_name", "first_name",
                    "last_name", "is_active", "is_staff", 'user_type', 'department', 'is_verified')

    fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'date_of_joining', 'department', 'degree')
        }),

        ('User Profile', {
            'classes': ('wide',),
            'fields': ('profile',)
        }),


        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )

    add_fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'date_of_joining', 'department', 'degree')
        }),

        ('User Profile', {
            'classes': ('wide',),
            'fields': ('profile',)
        }),


        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )


@admin.register(HOD)
class HODAdminConfig(UserAdmin):
    ordering = ("email",)
    list_display = ('id', "email", "user_name", "first_name",
                    "last_name", "is_active", "is_staff", 'user_type', 'department', 'is_verified')

    fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'date_of_joining', 'department', 'degree')
        }),

        ('User Profile', {
            'classes': ('wide',),
            'fields': ('profile',)
        }),


        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )
    add_fieldsets = (
        ('Mandatory Details', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'date_of_joining', 'department', 'degree')
        }),

        ('User Profile', {
            'classes': ('wide',),
            'fields': ('profile',)
        }),


        ('Type of User', {
            'classes': ('wide',),
            'fields': ('user_type', 'is_active', 'is_staff', 'is_verified')
        })
    )
