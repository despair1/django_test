# -*- coding: utf-8 -*-
'''
Created on 4 окт. 2015 г.

@author: despair
'''

from login import views
from django.conf.urls import  url


urlpatterns=(url(r"^login",views.loginview,name="loginview"),
             #url(r"^test.json$",views.test_json),
             url(r'^signup/', views.sign_up_in,name="sign_up"),
             )
