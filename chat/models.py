from django.db import models

# Create your models here.

class Message (models.Model):
    message_text = models.CharField(max_length=10000)
    message_users = models.CharField(max_length=200)
    message_timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.message_users
