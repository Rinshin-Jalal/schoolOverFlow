from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .models import User, EmailVerify
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from . import serializers
from django_rest_passwordreset.signals import reset_password_token_created


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.SignUp
    permission_classes = [permissions.AllowAny]


# Reset password

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'token': reset_password_token.key,
        'link': 'localhost:3000',  # your main frontend link
    }

    # render email text
    email_html_message = render_to_string(
        'authentication/user_reset_password.html', context)
    email_plaintext_message = render_to_string(
        'authentication/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="My Website"),
        # message:
        email_plaintext_message,
        # from:
        "rinzcodemail@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


class EmailVerifyView(generics.CreateAPIView):
    queryset = EmailVerify.objects.all()
    serializer_class = serializers.EmailVerifySerializer
    permission_classes = [permissions.AllowAny]
