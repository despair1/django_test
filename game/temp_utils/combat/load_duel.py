# -*- coding: utf-8 -*-
'''
Created on 7 нояб. 2015 г.

@author: despair
'''

from game.models import unit,player,combat_status

def load_duel(attaker):
    duel={}
    i=attaker
    duel["pk"]=i.pk
    #duel["round"]=0
    duel["rounds"]=[]
    #combatants.append(duel)
    if i.combat_status != combat_status.battle_loop:
        i.combat_status = combat_status.battle_loop
        i.save()
    return duel