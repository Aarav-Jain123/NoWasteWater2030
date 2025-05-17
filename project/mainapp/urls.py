from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='Home'),
    path('sign-up/', sign_up_page, name='Signup up'),
    path('login-in/', login_in_page, name='Login'),
    path('log-out/', logout_page, name='Logout'),
    path('delete-user/', delete_user_page, name='Delete user'),
    path('rewards/', books_page, name='Rewards'),
]
