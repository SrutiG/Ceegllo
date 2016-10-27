from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from gpacalc.models import Student
from .forms import LoginForm

def index(request):
    if not request.session.get('login'):
        return redirect('login')
    else:
        return redirect('home')

def login(request):
    return render(request, 'gpacalc/login.html')

def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = Student.objects.get(username = username, password = password)
    if len(user) > 0:
        request.session['login'] = True
        request.session['user'] = user
        return redirect('home')
    else:
        return redirect('login')


def home(request):
    return render(request, 'gpacalc/home.html')
