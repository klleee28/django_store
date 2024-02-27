from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),


    # Email Verification Url's
    path('email-verification', views.email_verification, name='email-verfication'),
    path('email-verification-sent', views.email_verification_sent, name='email-verfication-sent'),
    path('email-verification-success', views.email_verification_success, name='email-verfication-success'),
    path('email-verification-failed', views.email_verification_failed, name='email-verfication-failed'),

]