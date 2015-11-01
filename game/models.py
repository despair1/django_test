from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# placed in attacker unit
class combat_status():
    found_battle = 1
    battle_loop = 2
    

class player(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    name = models.CharField(max_length=10)

class battle(models.Model):
    b_time = models.DateTimeField()
    #attacker = models.OneToOneField()

class unit(models.Model):
    name = models.CharField(max_length=10)
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    #in_move = models.BooleanField()
    in_move = models.DateTimeField(null=True)
    user = models.ForeignKey(player)
    in_combat = models.ForeignKey('self',null=True)
    combat_status = models.IntegerField(null=True)
    #attacker = models.OneToOneField(battle,null=True)
    #defender = models.OneToOneField(battle,null=True)
    
