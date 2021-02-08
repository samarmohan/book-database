from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users.views import register_view

urlpatterns = [
    path("register/", register_view),
    path("login/", LoginView.as_view(template_name="login.html", redirect_authenticated_user=True)),
    path("logout/", LogoutView.as_view(template_name="logout.html")),
    path("password-reset/", PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>", PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path("register/", register_view),
]
