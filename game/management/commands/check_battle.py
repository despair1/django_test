# -*- coding: utf-8 -*-
'''
Created on 1 нояб. 2015 г.

@author: despair
'''

from django.core.management.base import BaseCommand
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from django.contrib.auth.models import User
from game.models import unit,player,combat_status
from game.temp_utils.combat.load_duel import load_duel
from django.db import connection
from time import sleep,clock

combats=[]

class Command(BaseCommand):
    help = " update units representation "
    
    def handle(self, *args, **options):
        try:
            cursor = connection.cursor()
            cursor.execute('begin')
            cursor.execute('LOCK TABLE game_unit')
            combatants = unit.objects.exclude(combat_status__isnull=True)
            for i in combatants:
                combats.append(load_duel(i))
                print "combatants ",i.x_pos,i.y_pos,i.user.user
        finally:
            cursor.execute('commit')
        while True:
            sleep(1)
            combatants = unit.objects.filter(combat_status=combat_status.found_battle)
            for i in combatants:
                combats.append(load_duel(i))
                print "new battle ",i.x_pos,i.y_pos,i.user.user
                redis_publisher=RedisPublisher(facility='units_updated',
                                                users=[i.user.user,i.in_combat.user.user])
                welcome = RedisMessage("begin battle "+str(i.pk))
                redis_publisher.publish_message(welcome)