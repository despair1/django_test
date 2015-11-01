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

class Command(BaseCommand):
    help = " update units representation "
    
    def handle(self, *args, **options):
        combatants = unit.objects.exclude(combat_status__isnull=True)
        for i in combatants:
            print "combatants ",i.x_pos,i.y_pos,i.user.user