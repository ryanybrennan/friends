from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt
from django.contrib.auth import password_validation
# Create your views here.
def index(request):
    return redirect('login_reg')
def login_reg(request):
    return render(request, 'login_reg/login_reg.html')
def process(request):
    register = User.UserManager.register(request.POST)
    if register[0] == False:
        password = request.POST['password'].encode()
        pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
        User.objects.create(name = request.POST['name'], alias= request.POST['alias'], email = request.POST['email'], password = pwhash, birthday = request.POST['birthday'])
        messages.add_message(request, messages.INFO, "You have registered!")
        return redirect(reverse('login_reg'))
    else:
        errors = register[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect(reverse('login_reg'))
def login(request):
    login = User.UserManager.login(request.POST)
    if login[0] == True:
        request.session['user'] = login[1].id
        return redirect(reverse('homepage'))
    else:
        errors = login[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect(reverse('login_reg'))
def logoff(request):
    del request.session['user']
    return redirect(reverse('login_reg'))
