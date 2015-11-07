# -*- coding: utf-8 -*-
'''
Created on 12 окт. 2015 г.

@author: despair
'''
from time import sleep,clock
from django.core.management.base import BaseCommand
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from django.contrib.auth.models import User
from game.models import unit,player,combat_status
from datetime import datetime,timedelta
#from django.utils import timezone
from django.db import connection
from game.temp_utils.combat.found_combat import found_combat

class Command(BaseCommand):
    help = " update units representation "
    
    def handle(self, *args, **options):
        welcome = RedisMessage('Hello everybody')
        print "begin update unit pos"
        redis_publisher=RedisPublisher(facility='units_updated', users=[x for x in User.objects.all()])
        
        while True:
            sleep(1)
            start=clock()
            #self.stdout.write( "ruslix " )
            try:
                cursor = connection.cursor()
                cursor.execute('begin')
                cursor.execute('LOCK TABLE game_unit')
                #cursor.fetchone()
                d=datetime.now()
                t=unit.objects.filter(in_move__lte=d)
                for i in t:
                    i.in_move=None
                    i.save()
                    found_combat(i)
                    """for ii in neighbor:
                        print ii.user.user," lalala3  ",i.user.user
                    """
                    redis_publisher=RedisPublisher(facility='units_updated', users=[i.user.user,])
                    welcome = RedisMessage("unit moved "+str(i.pk))
                    redis_publisher.publish_message(welcome)
                    print i.pk,i.in_move,i.user
            finally:
                cursor.execute('commit')
                
            #redis_publisher.publish_message(welcome)
            #self.stdout.write( str(clock()-start) )
    
