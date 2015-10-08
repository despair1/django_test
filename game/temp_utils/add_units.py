# -*- coding: utf-8 -*-
'''
Created on 8 окт. 2015 г.

@author: despair
'''
from django.http import JsonResponse
import json
from game.models import unit,player
from django.conf.global_settings import X_FRAME_OPTIONS

def add_unit(request):
    jd=json.loads(request.body)
    print "ai ai ai",jd
    print request.user
    p=player.objects.get(user=request.user)
    u=unit(name="1",x_pos=jd['x'],y_pos=jd['y'],
           in_move=False,user=p)
    u.save()
    #print "ai ai ai"
    return JsonResponse({})