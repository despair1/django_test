# -*- coding: utf-8 -*-
'''
Created on 4 окт. 2015 г.

@author: despair
'''
from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_slug

class sigh_up_form(forms.Form):
    username=forms.CharField(max_length=20,
                             validators=[validate_slug,])
    email=forms.EmailField(max_length=40)
    password=forms.CharField(max_length=255,widget=forms.PasswordInput)
    def clean_username(self):
        uname=self.cleaned_data['username']
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("username exists",code="username")
        return uname