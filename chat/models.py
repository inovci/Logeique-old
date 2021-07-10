from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):

=======
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_rooms")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_rooms")
    #code = models.CharField(unique = True , max_length = 250 )
>>>>>>> 0db2d56aa564a8a112f31fd169cb36ed2c269b1e

class Message(models.Model):
    value = models.TextField(max_length=100000, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_messages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_messages")
