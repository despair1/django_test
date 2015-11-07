# -*- coding: utf-8 -*-
'''
Created on 7 нояб. 2015 г.

@author: despair
'''

from django.http import JsonResponse
from game.models import unit,player
from django.db import connection

def send_battles_list(request):
    j={}
    j["defenders"]=[]
    j['attackers']=[]
    p=player.objects.get(user=request.user)
    u=unit.objects.filter(user=p,in_combat__isnull=False)
    for i in u:
        b={}
        b["x_pos"]=i.x_pos
        b["y_pos"]=i.y_pos
        if i.combat_status :
            j["attackers"].append(b)
        else :
            j["defenders"].append(b)
    return JsonResponse(j)
