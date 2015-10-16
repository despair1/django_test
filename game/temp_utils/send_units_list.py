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
    j={}
    """"j={"max":50,
       "own":[
              [1,2,50],
              [2,3,15],
              [3,7,45]]}"""
    p=player.objects.get(user=request.user)
    #print p.user.pk
    cursor.execute("""select max(a1) from (
    select count(*) as a1 from game_unit 
    where user_id=%s and in_move is null group by x_pos,y_pos) as foo;""",
    [p.user.pk])
    #print "bfg", cursor.fetchone()[0]
    j["max"]=cursor.fetchone()[0]
    cursor.execute("""select x_pos,y_pos,count(*) from game_unit
    where user_id=%s and in_move is null group by x_pos,y_pos;""",[p.user.pk])
    #print "bfg2"#,cursor.fetchall()
    #for i in connection.queries:
    #    print i
    j["own"]=cursor.fetchall()
    cursor.execute("""select id,x_pos,y_pos from game_unit
    where user_id=%s and in_move is null order by id;""",[p.user.pk])
    j["own_units_pos"]=cursor.fetchall()
    #print j["own_units_pos"]
    """"q=unit.objects.filter(user=p.user.pk)
    for i in q:
        print i"""
    return JsonResponse(j)
