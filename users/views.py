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


# Register view
def register_view(request):
    # Makes sure it is a post request
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        # Save the user
        user = form.save(commit=False)
        # But make them not active. If a user is not active, they are basically not created.
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        # The message using variables passed in.
        message = render_to_string('users/email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to = form.cleaned_data.get('email')
        # Sends email using email template.
        send_mail("Activate your account", message, os.environ.get("EMAIL_USER"), [to], html_message=message)
        # Display success message in template
        messages.success(request, f"{first_name}, your account was created! Please check your email!")

    return render(request, "users/register.html", {"form": form})


# The view that activates the account after you click the link
def activate_view(request, uidb64, token):
    # Try to decode the code in the link
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    # Otherwise throw errors.
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # Make the user active after the link is valid
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "users/confirm_email_complete.html")
    else:
        return HttpResponse('Activation link is invalid!')
