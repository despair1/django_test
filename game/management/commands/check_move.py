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
class Command(BaseCommand):
    help = " update units representation "
    def handle(self, *args, **options):
        welcome = RedisMessage('Hello everybody')
        redis_publisher=RedisPublisher(facility='units_updated', users=[x for x in User.objects.all()])
        while True:
            sleep(1)
            start=clock()
            self.stdout.write( "ruslix " ) 
            redis_publisher.publish_message(welcome)
            self.stdout.write( str(clock()-start) )
    
