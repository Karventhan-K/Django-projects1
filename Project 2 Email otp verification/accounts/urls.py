from django import views
from django.urls import path
from .views import*

urlpatterns = [
    path('create/', SignUpView.as_view(), name='Create'),
    path('otp-verification/', OtpVerifyView.as_view(),name = "Otp-verify"),
    path('login/', LoginApiView.as_view(), name='Login'),
    path('logout/', LogoutApiView.as_view(), name='Logout'),
]