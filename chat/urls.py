from django.conf.urls import url,include
from chat import views
urlpatterns =[
    url(r'^dashboard/', views.dashboard, name= 'dashboard'),
    url(r'^chatroom/(?P<id>[0-9A-Za-z_\-]+)/$', views.chat_room, name='chat_room'),
]
