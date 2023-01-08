from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response

from email_system.settings import EMAIL_HOST_USER
from .models import CustomUser
from .serializers import CustomUserSerializer, SendMailSerializer
from rest_framework import permissions
from django.core.mail import send_mail


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SendEmailAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SendMailSerializer
    permission_classes = [permissions.IsAdminUser]

    def send_mail(self, request, *args, **kwargs):
        subject= SendMailSerializer.subject
        message = SendMailSerializer.content
        # email = SendMailSerializer.email
        from_email = EMAIL_HOST_USER
        recipient_list = 'SendMailSerializer.email'

        send_mail(subject, message, from_email, recipient_list)


