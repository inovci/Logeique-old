from rest_framework import serializers
from chat.models import Message, Room


# Classe pour sérialiser tout message.
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


# Classe pour sérializer tout room (salle de chat).
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
