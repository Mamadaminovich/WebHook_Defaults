import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from .models import *

def home(request):
    return HttpResponse('Salom Dunyo')

TOKEN = '6719577695:AAGtoIx7smO8T-fDsPHDgQ3AxDeNL1lzOSc'
URL = 'https://ca96-213-230-76-159.ngrok-free.app/getpost/'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/'

def setwebhook(request):
    response = requests.post(TELEGRAM_API_URL + "setWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")

@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        update = json.loads(request.body.decode('utf-8'))
        handle_update(update)
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest('Bad Request')

def handle_update(update):
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    send_message("sendMessage", {
        'chat_id': chat_id,
        'text': f'you said {text}'
    })

def send_message(method, data):
    response = requests.post(TELEGRAM_API_URL + method, json=data)
    return response