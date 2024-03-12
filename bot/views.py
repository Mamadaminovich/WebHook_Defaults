from django.shortcuts import render, HttpResponse
from .models import *

def home(context):
    return HttpResponse('Salom Dunyo')