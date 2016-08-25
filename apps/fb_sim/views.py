from django.shortcuts import render, HttpResponse, redirect
from ..login_reg.models import User
from .models import Friendship
from django.db.models import Q

# Create your views here.
def friends(request):
    users = User.objects.all()
    pals = Friendship.objects.all()
    context={
    'users': User.objects.get(id=request.session['user']),
    'friends': Friendship.objects.filter(user__id = request.session['user']),
    'others': User.objects.exclude(id=request.session['user'])
    }
    print "*"*50
    print User.objects.filter(Q(userfriend__id = request.session['user']) & Q(friendfriend__id = request.session['user']))
    print "*"*50
    print User.objects.all()
    print "*"*50
    print Friendship.objects.all()
    return render(request, 'fb_sim/friends.html', context)
def profile(request, id):
    context = {
    'user': User.objects.get(id=id),
    }
    return render(request, 'fb_sim/profile.html', context)
def add(request, id):
    friend = Friendship.objects.create(user = User.objects.get(id=request.session['user']), friend = User.objects.get(id=id))
    user = Friendship.objects.create(user = User.objects.get(id=id), friend = User.objects.get(id=request.session['user']))
    friend.save()
    return redirect('homepage')
def remove(request, id):
    friend = Friendship.objects.filter(friend__id=id, user__id = request.session['user'])
    friend.delete()
    user = Friendship.objects.filter(user__id=id, friend__id = request.session['user'])
    user.delete()
    return redirect('homepage')
