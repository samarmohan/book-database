import os

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegisterForm

UserModel = get_user_model()


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        message = render_to_string('users/email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to = form.cleaned_data.get('email')
        send_mail("Activate your account", message, os.environ.get("EMAIL_USER"), [to], html_message=message)
        messages.success(request, f"{username}, your account was created! Please check your email!")

    return render(request, "users/register.html", {"form": form})


def activate_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "users/confirm_email_complete.html")
    else:
        return HttpResponse('Activation link is invalid!')
