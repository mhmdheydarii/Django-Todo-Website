from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_superuser", "created_date", "updated_date"]
    ordering = ('created_date',) 
    
    fieldsets = (
        ("Authentication", {"fields":("email", "created_date", "updated_date")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Groupe Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important Date", {"fields": ("last_login",)})
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)