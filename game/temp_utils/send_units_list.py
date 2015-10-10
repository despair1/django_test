# -*- coding: utf-8 -*-
'''
Created on 8 окт. 2015 г.

@author: despair
'''
from django.http import JsonResponse
from game.models import unit,player
from django.db import connection

def send_units_list(request):
    cursor=connection.cursor()
    j={"max":50,
       "own":[
              [1,2,50],
              [2,3,15],
              [3,7,45]]}
    p=player.objects.get(user=request.user)
    print p.user.pk
    cursor.execute("""select max(a1) from (
    select count(*) as a1 from game_unit 
    where user_id==%s group by x_pos,y_pos);""",
    [p.user.pk])
    #print "bfg", cursor.fetchone()[0]
    j["max"]=cursor.fetchone()[0]
    cursor.execute("""select x_pos,y_pos,count(*) from game_unit
    where user_id==%s group by x_pos,y_pos;""",[p.user.pk])
    print "bfg2"#,cursor.fetchall()
    for i in connection.queries:
        print i
    j["own"]=cursor.fetchall()
    return JsonResponse(j)
