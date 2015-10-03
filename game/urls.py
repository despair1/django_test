# -*- coding: utf-8 -*-
'''
Created on 2 окт. 2015 г.

@author: despair
'''
from game import views
from django.conf.urls import  url


urlpatterns=(url(r"^$",views.index,name="index"),
             url(r"^test.json$",views.test_json),
             )