from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Message

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
import datetime

from chat.forms import(
user_registration_form,
send_message_form,
)
# Create your views here.

def index (request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return render(request,"index.html",{})

def registration(request):
    if request.method == 'POST':
        form_registration = user_registration_form(request.POST)
        if form_registration.is_valid():
            form_registration.save()
            username = form_registration.cleaned_data.get('username')
            raw_password = form_registration.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login(request,user)
            return redirect('dashboard')
    else:
        form_registration = user_registration_form()
    return render(request, 'registration/registration.html', {'form_registration': form_registration})



def dashboard(request):
    queryUsers = User.objects.exclude(id = request.user.id)
    return render (request, 'dashboard.html',{'queryUsers': queryUsers})

def chat_room (request,id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_send_message = send_message_form(request.POST)
            if form_send_message.is_valid():
                message = form_send_message.save(commit=False)
                message.message_timestamp = datetime.datetime.now()
                queryChattingWithUserID = User.objects.get(id=id)
                queryChattingFromUserID = User.objects.get(id=request.user.id)
                message_from_user = request.user
                message.message_users = str(min(queryChattingWithUserID.id , queryChattingFromUserID.id)) + "/" + str(max(queryChattingWithUserID.id , queryChattingFromUserID.id))
                message.message_text = (str(message_from_user)+": " + message.message_text)
                message.save()
            return HttpResponseRedirect('.')
        else:
            form_send_message = send_message_form()
            queryChattingWithUser = User.objects.filter(id=id)
            queryChattingFromUser = User.objects.filter(id=request.user.id)

            queryChattingWithUserID = User.objects.get(id=id)
            queryChattingFromUserID = User.objects.get(id=request.user.id)
            message_users_id = str(min(queryChattingWithUserID.id , queryChattingFromUserID.id)) + "/" + str(max(queryChattingWithUserID.id , queryChattingFromUserID.id))
            messages_between_users= Message.objects.filter(message_users = message_users_id)
            return render(request, 'chatroom/chatroom.html', {
                'form_send_message': form_send_message,
                "queryChattingWithUser" : queryChattingWithUser,
                "queryChattingFromUser" : queryChattingFromUser,
                "messages_between_users":messages_between_users,
                })
    else:
        return redirect('login')
