from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'candidate/login.html')

def signin(request):
    return render(request, 'signin.html')
