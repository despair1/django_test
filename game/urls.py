# -*- coding: utf-8 -*-
'''
Created on 2 окт. 2015 г.

@author: despair
'''
from game import views
from game.temp_utils import add_units
from django.conf.urls import  url


urlpatterns=(url(r"^$",views.index,name="index"),
             url(r"^test.json$",views.test_json),
             url(r"^units.json$",views.units_json),
             url(r"^send.json$",views.recive_json),
             url(r"^add_unit.json$",add_units.add_unit),
             )