# -*- coding: utf-8 -*-
'''
Created on 15 окт. 2015 г.

@author: despair
'''
from django.core.exceptions import PermissionDenied

def get_allowed_channels(request, channels):
    if not request.user.is_authenticated():
        raise PermissionDenied('Not allowed to subscribe nor to publish on the Websocket!')
    #print channels
    return channels