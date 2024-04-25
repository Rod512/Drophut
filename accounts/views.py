from django.shortcuts import render
from django.http import HttpResponseRedirect


def register(request):
    return render(request, 'accounts/register.html')

def user_login(request):
    return render(request, 'accounts/login.html')

def user_logout(request):
    return HttpResponseRedirect('/')
