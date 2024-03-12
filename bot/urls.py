from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('getpost/', telegram_bot, name='telegram_bot'),
    path('setwebhook/', setwebhook, name='setwebhook'),
]