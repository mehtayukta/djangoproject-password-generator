from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'yukmskfsgks'})

def password(request):

    chara =list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chara.extend(list('ABCDEFGHIJKLMNOPQURSTUVWXYZ'))
    if request.GET.get('number'):
        chara.extend(list('0123456789'))
    if request.GET.get('specail'):
        chara.extend(list('!@#$%^&*()'))    
    length= int(request.GET.get('length',8))

    thepassword =''

    for x in range(length):
        thepassword += random.choice(chara)
    return render(request, 'generator/password.html',{'password':thepassword})
def aboutus(request):
    return render(request, 'generator/aboutus.html', {'aboutus':'yukmskfsgks'})