# -*- coding: utf-8 -*-
'''
Created on 3 окт. 2015 г.

@author: despair
'''
import json
import random

data={"map_layer1":[]}
with open('/home/despair/evedev/phaser_test/assets/map_layer1','w') as of:
    for x in range(0,40):
        d=[]
        for y in range(0,30):
            d.append(random.randint(0,6))
        data['map_layer1'].append(d)
    json.dump(data,of)