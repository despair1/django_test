from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class player(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    name = models.CharField(max_length=10)

class unit(models.Model):
    name = models.CharField(max_length=10)
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    in_move = models.BooleanField()
    user = models.ForeignKey(player)
    
