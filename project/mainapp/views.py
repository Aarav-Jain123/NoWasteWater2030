from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


@api_view(['POST'])
def sign_up_page(request):
    auth_data = request.data
    
    request.session['name'] = request.data['name']
    request.session['email'] = request.data['email']
    request.session['password'] = request.data['password']
    request.session.set_expiry(300)
    
    auth_otp = otp_generator()
    send_otp(request.session['email'], auth_otp)
    
    res = [{'key': 0, 'response': 'Hello!'}]
    
    return Response(data=res)


@api_view(['POST'])
def login_in_page(request):
    auth_data = request.data
    
    request.session['email'] = request.data['email']
    request.session['password'] = request.data['password']
    request.session.set_expiry(300)
    
    auth_otp = otp_generator()
    send_otp(request.session['email'], auth_otp)
    
    res = [{'key': 0, 'response': 'Hello!'}]
    
    return Response(data=res)


def otp_generator():
    r1, r2, r3, r4, r5, r6 = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
    r = f'{r1}{r2}{r3}{r4}{r5}{r6}' 
    return r


def send_email(email, token):
    subject = 'Your OTP is here'
    msg = f'Hello User! Here is your otp: {token}. Hope you get the best response from our side!'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(subject, msg, from_email, recipients)


def send_otp(email, token):
    subject = 'Your OTP is here'
    msg = f'Here is your otp: {token}.'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(subject, msg, from_email, recipients)