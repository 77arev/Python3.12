from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
# def home(request):
#     return HttpResponse("Hello")

def home(request):
    lst = list(range(6, 15))
    # print(lst)
    return render(request, "generator/home.html", {'lst': lst})


# Здесь пишем папку (generator) и html
# , {'pas': 'qwerty'} - словарь, ключ-значение, через документ html (home.html) {{ pas }} выводится
# значение по ключу {{ pas }} - (qwerty) на страницу

# def password(request):
#     return render(request, "generator/password.html")


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length'))
    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})


def rules(request):
    return render(request, "generator/rules.html")
