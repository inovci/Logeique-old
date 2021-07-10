from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from spaces.models import Client , Landlord

# Create your models here.
class Room(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_rooms")
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name="landlord_rooms")
    code = models.CharField(unique = True , max_length = 250 )

class Message(models.Model):
    value = models.TextField(max_length=100000, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_messages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_messages")
