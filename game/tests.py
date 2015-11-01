from django.test import TestCase
from django.contrib.auth.models import User
from game.models import player
from game.temp_utils.add_units import add_unit,move_unit
from game.temp_utils.send_units_list import send_units_list
import json
from game.models import unit
from game.temp_utils.found_combat import found_combat
# Create your tests here.

def finalize_move():
    t=unit.objects.filter(in_move__isnull=False)
    for i in t:
        i.in_move=None
        i.save()

class FirstTestCase(TestCase):
    def setUp(self):
        user = User(username="lamer",
                    email="lamer@from.ru")
        user.set_password("password")
        user.save()
        p=player(name="username",
                user=user)
        p.save()
        user = User(username="lamer1",
                    email="lamer1@from.ru")
        user.set_password("password")
        user.save()
        p=player(name="username1",
                user=user)
        p.save()
        class request():
            user=User.objects.get(username="lamer")
            body="""{"x":1,"y":1}"""
        class request1():
            user=User.objects.get(username="lamer1")
            body="""{"x":1,"y":1}"""
        r=request()
        add_unit(r)
        r.body="""{"x":3,"y":4}"""
        add_unit(r)
        r=request1()
        add_unit(r)
    def test_1(self):
        class request():
            user=User.objects.get(username="lamer")
            #body="""{"x":1,"y":1}"""
        r=request()
        j=json.loads(send_units_list(r).content)
        self.assertEqual(j["max"],1)
        self.assertEqual(j["own_units_pos"][1],[2,3,4])
        #print j
        r.body="""{"x":5,"y":6,"id":2}"""
        move_unit(r)
        finalize_move()
        j=json.loads(send_units_list(r).content)
        print j
        self.assertEqual(j["own_units_pos"][1],[2,5,6])
        #print j
        #print "1"
        t=unit.objects.filter(in_combat__isnull=False)
        self.assertEqual(t.count(),0)
        found_combat(unit.objects.get(pk=1))
        t=unit.objects.filter(in_combat__isnull=False)
        self.assertEqual(t.count(),2)
        #print "second test ",t.count()
    #def test_fount_combat(self):
        #t=unit.objects.filter(in_combat__isnull=False)
        #print "second test ",t.count()
        #pass