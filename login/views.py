# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login/login.html', c)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def sign_up_in(request):
    post = request.POST
    """
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/login/")"""
# Create your views here.
