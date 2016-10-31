from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from gpacalc.models import Student
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    if not request.session.get('login'):
        return redirect('login')
    else:
        return redirect('home')

def login(request):
    request.session['login'] = False
    request.session['username'] = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Student.objects.get(username = username, password = password)
            request.session['login'] = True
            request.session['username'] = username
            return redirect('home')
        except ObjectDoesNotExist:
            return redirect('login')
    return render(request, 'gpacalc/login.html')

def home(request):
    username = request.session.get('username')
    user = Student.objects.get(username=username)
    college = user.collegename
    name = Student.__str__(user)
    return render(request, 'gpacalc/home.html', {'username': username, 'name': name, 'college' : college})

def register(request):
    yearchoices = Student.YEAR_CHOICES
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        year = request.POST.get('year')
        username = request.POST.get('username')
        password = request.POST.get('password')
        Student.objects.create(first_name = firstname, last_name = lastname, year = year,
                                         username = username, password = password)
        return redirect('login')
    return render(request, 'gpacalc/register.html', {'yearchoices':yearchoices})

def editcollege(request):
    username = request.session.get('username')
    return render(request, 'gpacalc/editcollege.html', {'username': username})

def editprofile(request):
    username = request.session.get('username')
    return render(request, 'gpacalc/editprofile.html', {'username': username})

def editfuture(request):
    username = request.session.get('username')
    return render(request, 'gpacalc/editfuture.html', {'username': username})

def currentclasses(request):
    username = request.session.get('username')
    return render(request, 'gpacalc/currentclasses.html', {'username': username})

def currentclass(request):
    username = request.session.get('username')
    return render(request, 'gpacalc/class.html', {'username': username})

