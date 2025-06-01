from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='Home'),
    path('signup/', sign_up, name='Signup'),
    # path('login/', login_in_page, name='Login'),
    # path('logout/', logout_page, name='Logout'),
    path('shop/', books_page, name='Rewards'),
    # path('otp/', otp_page, name='OTP'),
    path('your-profile/', your_profile_page, name='Your profile'),
    path('quiz/', quiz_page, name='Quiz'),
]
