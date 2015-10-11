# -*- coding: utf-8 -*-
'''
Created on 11 окт. 2015 г.

@author: despair
'''
from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def add5():
    #logger = add.get_logger()
    logger.info("Adding  SUUUUUUUUUKc")
    print "WTF &&&& ????"