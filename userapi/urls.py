
from django.urls import path, include
from userapi import views

urlpatterns = [
    path('', views.UserCreateAPIView.as_view(),  name= 'create_user'),
    path('<int:pk>/', views.UserDetailAPIView.as_view(), name= 'user_detail'),
    path('list/', views.UserListAPIView.as_view(), name= 'user_list'),
    path('mail/', views.SendEmailAPIView.as_view(), name= 'send_mail')
]
