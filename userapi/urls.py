
from django.urls import path, include
from userapi import views

urlpatterns = [
    path('user', views.UserCreateAPIView.as_view(),  name='create_user'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail'),
    path('users/', views.UserListAPIView.as_view(), name='user_list'),
    path('bulkmail/', views.SendBulkEmailAPIView.as_view(), name='send_mail'),
    path('mail/<int:pk>/', views.SendEmailAPIView.as_view(), name='send_mail')
]
