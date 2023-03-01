from django.shortcuts import redirect, render

from . import views
from django.urls import path



urlpatterns=[
    path('', views.Welcome, name='welcome'),
    path('chat-room/', views.chatRoom, name='chat-room'),

    path('get_token/' , views.getToken, name='get-token'),
    path('create_member/', views.createMember , name= 'create-member'),
    path('get_member/', views.getMember , name= 'get-member'),
    path('delete_member/', views.deleteMember , name= 'delete-member'),
]