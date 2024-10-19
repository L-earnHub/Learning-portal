from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
from datetime import timedelta
import requests
import json
from login.sqlQueries import XataApi
from login.otp import *

obj = XataApi("L-earn-Hub-s-workspace-3rj5i6", "us-east-1", "learnhub", "main","users", "xau_jIRNNlavLZ7IvkDYCPq3NwlAU4p15pR13")

# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('Email')
#         username = request.POST.get('username')
#         password1 = request.POST.get('Password')
#         password2 = request.POST.get('confirm_password')
#         if password1 == password2:
#             emailpresent = obj.isEmailPresent(email)
#             if emailpresent:
#                 messages.info(request,'email is already Registered')
#                 return redirect('signup')
#             elif username == obj.isUserNamePresent(username):
#                 messages.info(request,'username is taken')
#                 return redirect('signup')
#             else:
#                 data = {
#                     "username": username,
#                     "email": email,
#                     "password": password1, 
#                 }
#                 obj.insert_xata_record(data)
#                 messages.success(request, 'User created successfully! Please login.')
#                 return redirect('login')
#         else:
#             messages.info(request,'password doesnot match')
#             return render(request, 'signup.html')    
#     else:
#         return render(request,"signup.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')  
        email = request.POST.get('email')  
        password1 = request.POST.get('password')  
        password2 = request.POST.get('confirm_password') 

        if password1 == password2:
            is_email_present = obj.isEmailPresent(email)  
            if is_email_present:
                messages.info(request, 'This email is already registered.')
                return redirect('signup') 
            
            is_username_taken = obj.isUserNamePresent(name) 
            if is_username_taken:
                messages.info(request, 'This username is already taken.')
                return redirect('signup')  
            
            user_data = {
                "username": name,  
                "email": email,
                "password": password1, 
            }
            obj.insert_xata_record(user_data) 
            
            messages.success(request, 'User created successfully! Please login.') 
            return redirect('login') 
        
        else:
            messages.info(request, 'Passwords do not match.') 
            return render(request, 'signup.html') 
    
    else:
        return render(request, "signup.html") 



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_password_valid = obj.password_check(password)
        is_email_present = obj.isEmailPresent(email)

        if is_password_valid and is_email_present:
            otp = generate_otp()
            sendEmailCC(email, otp)
            request.session['otp'] = otp
            request.session['otp_sent_time'] = timezone.now().isoformat() 
            request.session.set_expiry(120)
            request.session['email'] = email
            return redirect('verify_otp')
        else:
            messages.error(request, 'Invalid credentials. Please check your email and password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

from django.http import JsonResponse

from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse

def resend_otp(request):
    if request.method == 'POST':
        otp_sent_time = request.session.get('otp_sent_time')
        if otp_sent_time:
            otp_sent_time = timezone.datetime.fromisoformat(otp_sent_time)
        if otp_sent_time and timezone.now() < otp_sent_time + timedelta(minutes=2):
            email = request.session.get('email')
            otp = generate_otp()
            sendEmailCC(email, otp)
            request.session['otp'] = otp
            request.session['otp_sent_time'] = timezone.now().isoformat()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'OTP request expired or invalid.'})




def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if stored_otp and entered_otp == str(stored_otp):
            messages.success(request, 'OTP verified successfully.')
            # return redirect('home')
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid or expired OTP. Please try again.')
            return render(request, 'otp.html')
    return render(request, 'otp.html') 

def home(request):
    return render(request, 'home.html')
