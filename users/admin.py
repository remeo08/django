from django.contrib import admin
from .models import User


# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("name", "age", "description", "is_business")

#     list_filter = ("is_business",) 
    
#     search_fields = ("name",)

from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile Info", {"fields": ("name", "email", "gender")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "age", "email", "is_business")
