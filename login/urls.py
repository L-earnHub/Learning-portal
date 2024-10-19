from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('otp',views.verify_otp,name='verify_otp'),
    # path('home',views.home,name='home'),
    path('resend_otp/',views.resend_otp,name='resend_otp'),
]