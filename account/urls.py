from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views
from .forms import PwdResetForm, PwdResetConfirmForm, UserLoginForm


app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login.html", form_class=UserLoginForm),
        name="login",
    ),
    path('logout/', views.logout_view, name='logout'),
    path('delete_user/', TemplateView.as_view(template_name="account/delete_confirm.html"), name='delete_user'),
    path('delete_user_confirm/<int:pk>/', views.delete_user, name='delete_user_confirmation'),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset_form.html",
            success_url="password_reset_email_confirm/",
            email_template_name="account/password_reset_email.html",
            form_class=PwdResetForm
        ),
        name='pwdreset',
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html',
            success_url='password_reset_complete/',
            form_class=PwdResetConfirmForm,
        ),
        name='password_reset_confirm'  
    ),
    path(
        'password_reset/password_reset_email_confirm/',
        TemplateView.as_view(template_name='account/reset_status.html'),
        name='password_reset_done',
    ),
    path(
        'password_reset_confirm/Nw/set-password/password_reset_complete/',
        TemplateView.as_view(template_name='account/reset_status.html'),
        name='password_reset_complete'
    ),
    # path("edit/", views.edit_details, name="edit_details"),
    ]
