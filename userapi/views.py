from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings
from rest_framework.response import Response
from email_system.settings import EMAIL_HOST_USER
from .models import CustomUser
from .serializers import CustomUserSerializer, SendMailSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAdminUser]


class UserDetailAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]


class SendBulkEmailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_users(self):
        queryset = CustomUser.objects.all()
        return queryset

    def send_email(self, emails):
        subject = "Test Email"
        message = "Message Content"
        msg1 = (subject,
                message,
                settings.EMAIL_HOST_USER,
                emails)
        response = send_mass_mail(
            (msg1,)
            ,
            fail_silently=False
        )
        import pdb;
        pdb.set_trace()

    def post(self, request, *args, **kwargs):
        user_queryset = self.get_users()
        emails = user_queryset.values_list('email', flat=True)
        self.send_email(list(emails))
        return Response()


class SendEmailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_user(self, pk):
        queryset = CustomUser.objects.get(pk=pk)
        return queryset

    def send_email(self, email):
        subject = "Test single Email"
        message = "Message single Content"
        # msg1 = (subject,
        #         message,
        #         settings.EMAIL_HOST_USER,
        #         email)
        response = send_mail(subject, message,settings.EMAIL_HOST_USER, [email],
                             fail_silently=False
                             )
        # import pdb;
        # pdb.set_trace()

    def post(self, request, pk, *args, **kwargs):
        user_queryset = self.get_user(pk=pk)
        email = user_queryset.email
        self.send_email(email)
        return Response()
