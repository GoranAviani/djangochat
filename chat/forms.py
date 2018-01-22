from django import forms
from django.contrib.auth.models import User
from chat.models import Message
from django.contrib.auth.forms import UserCreationForm

class user_registration_form(UserCreationForm):
    model = User
    fields = (
        'username',
        'email',
        'password1',
        'password2',
    )

class send_message_form(forms.ModelForm):
    message_text = forms.CharField(label='',  widget=forms.TextInput(attrs={'class':'chat-input'}))
    class Meta:
        model = Message
        fields = (
            'message_text',
            )
#widget=forms.TextInput(attrs={'size':40})
