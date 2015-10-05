# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse 
from django.db import IntegrityError 
from django.core.validators import RegexValidator
from login.forms import sigh_up_form,sign_in_form

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
def logout_view(request):
    logout(request)
    return redirect("login:sign_in")
    
def sign_in(request):
    c = {}
    c.update(csrf(request))
    c['username']=request.user.username
    if request.method=='POST':
        c["form"]=sign_in_form(request.POST)
        #c["error_message"]="vvedena forma"
        if c['form'].is_valid():
            f=c['form']
            u=authenticate(username=f.cleaned_data["username"],
                           password=f.cleaned_data["password"])
            #print u
            login(request,u)
            
            #print "valid"
            return redirect('game:index')
    else:
        c["form"]=sign_in_form()
    return render_to_response('login/sign_in.html', c) 
def sign_up_in(request):
    c = {}
    c.update(csrf(request))
    if request.method=='POST':
        c["form"]=sigh_up_form(request.POST)
        #c["error_message"]="vvedena forma"
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
            return redirect('game:index')
            print "valid"
    else:
        c["form"]=sigh_up_form()
    return render_to_response('login/sign_up.html', c) 
    
# Create your views here.
