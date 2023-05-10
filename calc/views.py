from django.shortcuts import render
from django.http import HttpResponse
import pyrebase


firebaseConfig = {
    ' apiKey': "AIzaSyCSu0FoWcCsZZlPsGXwARQ78Y37JcMfNB0",
    'authDomain': "djangodb-a0875.firebaseapp.com",
    'databaseURL': "https://djangodb-a0875-default-rtdb.firebaseio.com",
    'projectId': "djangodb-a0875",
    'storageBucket': "djangodb-a0875.appspot.com",
    'messagingSenderId': "906292872887",
    'appId': "1:906292872887:web:b07000caed5699d62eaf32",
    'measurementId': "G-P0CPNEC7B2"
}


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Navin'})


def add(request):
    value1 = request.POST['num1']
    value2 = request.POST['num2']
    res = int(value1) + int(value2)
    return render(request, 'resullt.html', {'result': res})


def subtract(request):
    value1 = request.GET['num1']
    value2 = request.GET['num2']
    res = int(value1) - int(value2)
    return render(request, 'resullt2.html', {'result2': res})
