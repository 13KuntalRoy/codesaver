from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt.token_blacklist import models
from rest_framework_simplejwt.token_blacklist.admin import \
    OutstandingTokenAdmin

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import USER


class USERAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = USER
    list_display = (
        "email",
        "username",
        "auth_provider"
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "username", "password",)}),
        ("Permissions", {"fields": ("is_staff", "is_active",
         "is_email_verified")}),
    )
    readonly_fields = (
        "id",
        # "type",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_email_verified",
                    # "type",
                    "auth_provider",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class NewOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)
admin.site.register(USER, USERAdmin)
