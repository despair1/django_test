# -*- coding: utf-8 -*-
'''
Created on 8 окт. 2015 г.

@author: despair
'''
from django.http import JsonResponse
import json
from game.models import unit,player
from django.conf.global_settings import X_FRAME_OPTIONS
from django.db import connection
import sys
from django.db import IntegrityError
def add_unit(request):
    jd=json.loads(request.body)
    #print "ai ai ai",jd
    #print request.user
    #print jd
    p=player.objects.get(user=request.user)
    #print p.user,p.name
    u=unit(name="1",x_pos=jd['x'],y_pos=jd['y'],
           #in_move=False,user=p)
           user=p)
    #print u
    #for i in connection.queries:
    #    print i
    #try:
    u.save() 
    """
    except IntegrityError as e:
        print e.message
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print "ai ai ai" """
    return JsonResponse({})

def move_unit(request):
    jd=json.loads(request.body)
    p=player.objects.get(user=request.user)
    u=unit.objects.get(pk=jd['id'])
    if u.user == p:
        u.x_pos=jd['x']
        u.y_pos=jd['y']
        u.save()
        return JsonResponse({})
    