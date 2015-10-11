from django.test import TestCase
from django.contrib.auth.models import User
from game.models import player
from game.temp_utils.add_units import add_unit
from game.temp_utils.send_units_list import send_units_list
import json
# Create your tests here.
class FirstTestCase(TestCase):
    def setUp(self):
        user = User(username="lamer",
                    email="lamer@from.ru")
        user.set_password("password")
        user.save()
        p=player(name="username",
                user=user)
        p.save()
        class request():
            user=User.objects.get(username="lamer")
            body="""{"x":1,"y":1}"""
        r=request()
        add_unit(r)
    def test_1(self):
        class request():
            user=User.objects.get(username="lamer")
            #body="""{"x":1,"y":1}"""
        r=request()
        j=json.loads(send_units_list(r).content)
        self.assertEqual(j["max"],1)
        #print "1"
        