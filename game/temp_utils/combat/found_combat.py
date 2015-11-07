# -*- coding: utf-8 -*-
'''
Created on 1 нояб. 2015 г.

@author: despair
'''
from game.models import unit,combat_status

def found_combat(attacker):
    i=attacker
    neighbor=unit.objects.filter(x_pos=i.x_pos)\
        .filter(y_pos=i.y_pos).filter(in_move=None,in_combat=None)\
        .exclude(user=i.user)
    if neighbor.exists():
        print "exists"
        n=neighbor[0]
        i.in_combat=n
        i.combat_status=combat_status.found_battle
        n.in_combat=i 
        i.save()
        n.save()