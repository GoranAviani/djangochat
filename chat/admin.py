from django.contrib import admin
from chat.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("message_users","message_text","message_timestamp")


admin.site.register(Message,MessageAdmin)
