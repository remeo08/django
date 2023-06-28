from django.contrib import admin
from .models import Chatting

# Register your models here.
@admin.register(Chatting)
class ChattingAdmin(admin.ModelAdmin):
    pass