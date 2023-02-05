from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Role, Team, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(userAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUseerChangeForm
    add_fieldsets  = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
         (None, {"fields": ("role", "team")}),
    )

    admin.site.register(CustomUser, UserAdmin)
    admin.site.register({Role, Team})
# Register your models here.
