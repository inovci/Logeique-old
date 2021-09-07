from rest_framework import serializers
from chat.models import Message, Room
from spaces.models import Deal


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


# Classe pour sérializer tout deal.
class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
