from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=2000) #name of room

class Message(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True) #Time msg was sent
    value = models.CharField(max_length=5000000) #info on the msg
    room = models.CharField(max_length= 50000) #room where msg was sent
    user = models.CharField(max_length=2000) #The sender of the msg


