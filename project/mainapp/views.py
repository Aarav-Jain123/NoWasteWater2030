from rest_framework.decorators import api_view
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from random import randint
from django.shortcuts import render, redirect
from django.contrib import messages
import random
import json
from . import JSONops

# Create your views here.
@api_view(['GET'])
def index_page(request):
    if request.user.is_anonymous:
        res = [{'key': 0, 'response': "False"}]
    else:
        res = [{"key": 0, 'response': 'True'}]           
    return Response(data=res)


@api_view(['POST'])
def login_in_page(request):
    auth_data = request.data
    
    request.session['email'] = auth_data['email']
    request.session['password'] = auth_data['password']
    request.session.set_expiry(300)
    
    try:
        user = authenticate(username=request.session['email'], password=request.session['password'])

        if user is not None:
            request.session['auth_otp'] = otp_generator()
            send_otp(request.session['email'], request.session['auth_otp'])

            res = [{'key': 0, 'response': 'OTP sent successfully, please check your inbox and spam folders!'}]

        else:
            res = [{'key': 0, 'response': 'Invalid credentials, please double check your credentials or go to /signup .'}]   
    except Exception as e:
        res = [{'key': 0, 'response': e}]
            
    return Response(data=res)


def otp_generator():
    r1, r2, r3, r4, r5, r6 = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
    r = f'{r1}{r2}{r3}{r4}{r5}{r6}'
    return r


def send_otp(email, token):
    subject = 'Your OTP is here'
    msg = f'Here is your otp: {token}.'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(subject, msg, from_email, recipients)
    

def authenticate_user(userr_id):
    userr = UserProfile.objects.filter(user_id=userr_id).exists()
    
    return userr


def extract_parameters(userr_id):
    userr = UserProfile.objects.get(user_id=userr_id)
    pr = {'coins': userr.user_points, 'name': userr.name, 'email': userr.email, "themes_owned": None, 'logos_owned': None}
    return pr


def add_user(request):
    user = authenticate(username=request.session['email'], password=request.session['password'])
    if user is not None:
        login(request, user)
    if user is None:
        user = User.objects.create_user(username=request.session['email'], name=request.session['name'], email=request.session['email'])
        user.set_password(request.session['password'])
        user.save()
        
        custom_user = UserProfile.objects.create(user=user)
        custom_user.save()
        

@api_view(['POST'])
def logout_page(request):
    logout(request)
    
    res = [{'key': 0, 'response': 'Hello!'}]
    
    return Response(data=res)


@api_view(['POST'])
def delete_user_page(request):
    auth_data = request.data
    username_of_user = request.user.username
    
    try:
    
        user = authenticate(username=username_of_user, password=auth_data['password'])
        if user:
            user.objects.delete()
            res = [{'key': 0, 'response': 'User deleted successfully!'}]
        
            return Response(data=res)
        else:
            res = [{'key': 0, 'response': 'Something seems wrong, please check your credentials.'}]
        
    except Exception as e:
        res = [{'key': 0, 'response': e}]
    
    return Response(data=res)


@api_view(['POST'])
def add_coins(request):
    data = request.data
    
    email_id = data['email']
    coins_to_add = data['coinsToAdd']
    
    user = UserProfile.object.get(email=email_id)
    user.user_points = user.user_points + coins_to_add
    
    user.save()
    
    res = [{'key': 0, 'response': 'User points updated successfully!'}]
    
    return Response(data=res)


@api_view(['POST'])
def book_transaction(request):
    data = request.data
    
    book_id = data['bookId']
    
    book = Books.objects.get(id=book_id)
    bookPrice = book.price
    
    user_id = request.user.username
    
    user = UserProfile.objects.get(email=user_id)
    userPoints = user.user_points
    
    if userPoints >= bookPrice:
        user.user_points = userPoints - bookPrice
        user.save()
        
        book.bookss.add(user)
        
        res = [{'key': 0, 'message': 'Transaction made successful'}]
    else:
        res = [{'key': 0, 'message': 'Transaction not successful'}]
    
    return Response(data=res)

@api_view(['GET'])
def books_page(request): 
    if request.user.is_anonymous:
        res = [{'key': 0, 'response': "False"}]
    else:
        res = [{"key": 0, 'response': 'True'}]           
    return Response(data=res)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data.get('email'), password=form.data.get('password1'))
            if user is None:
                request.session['auth_token'] = otp_generator()
                request.session['signup_data'] = form.data
                send_otp(form.data.get('email'), request.session['auth_token'])
                request.session.set_expiry(300)
            else:
                messages.error(request, '''Seems like the account already exists, please go to /login.''')
                return redirect('/signup')
            return redirect('/otp')
    else:
        form = RegisterForm()
    
    logout(request)

    return render(request, 'registration/signup.html', {"form": form})


def otp_page(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        if otp == request.session['auth_token']:
            data = request.session['signup_data']
            user = User.objects.create_user(first_name=data.get('first_name'), username=data.get('email'), email=data.get('email'))
            user.set_password(data.get('password1'))
            user.save()
            
            custom_user = UserProfile.objects.create(userr=user, email=data.get('email'), name=data.get('first_name'))
            custom_user.save()
            login(request, user)
            return redirect('http://localhost:5173/')
        else:
            messages.error(request, 'Invalid OTP')            
    return render(request, 'registration/otp.html')


@api_view(['POST'])
def fact_abt_water(request):
    facts = JSONops.access_json_data('facts.json')
    
    
    # chosen = random.choice(facts)
    res = [{"key": 0, 'response': facts["facts"][randint(0, 9)]}]
    
    return Response(data=res)

@api_view(['POST'])
def quiz(request):
    mcqs = JSONops.access_json_data('water_climate_mcqs.json')
    start_and_end = lambda start=randint(0, len(mcqs)-6): (start,start+5)
    startq, endq = start_and_end()
    print(startq, endq)
    try:
        res = [{"key": 0, 'response': mcqs[startq:endq]}]
    except Exception as e:
        startq, endq = start_and_end()
        print(startq, endq)
        res = [{"key": 0, 'response': mcqs[startq:endq]}]

    return Response(data=res)