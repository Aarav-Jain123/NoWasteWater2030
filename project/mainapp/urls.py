from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='Index'),
    # path('home/', home_page, name='Home'),    
    path('signup/', sign_up, name='Signup'),
    path('shop/', books_page, name='Rewards'),
    path('otp/', otp_page, name='OTP'),
    path('your-profile/', your_profile_page, name='Your profile'),
    path('quiz/', quiz_page, name='Quiz'),
]
