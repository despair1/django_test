# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse 
from django.db import IntegrityError 
from django.core.validators import RegexValidator
from login.forms import sigh_up_form

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login/login.html', c)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user
rxv=RegexValidator('a')
def sign_up_in(request):
    c = {}
    c.update(csrf(request))
    if request.method=='POST':
        c["form"]=sigh_up_form(request.POST)
        c["error_message"]="vvedena forma"
        if c['form'].is_valid():
            f=c['form']
            user = User(username=f.cleaned_data["username"],
                         email=f.cleaned_data["email"])
            user.set_password(f.cleaned_data["password"])
            user.save()
            u=authenticate(username=user.username,
                           password=f.cleaned_data["password"])
            print u
            login(request,u)
            
            print "valid"
    else:
        c["form"]=sigh_up_form()
    return render_to_response('login/sign_up.html', c) 
    if request.method=='POST':
        pass
    post = request.POST
    try:
        create_user(username=post['uname'],email=post['email'],
                password=post['password'])
        rxv(post['uname'])
    except IntegrityError as e:
        c = {}
        c.update(csrf(request))
        c["error_message"]=e.message
        return render_to_response('login/login.html', c) 
    return redirect('login:loginview')
    """
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/login/")"""
# Create your views here.
