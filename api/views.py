from django.core.checks import messages
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.views import APIView

from .serializers import MessageSerializer, RoomSerializer
from chat.models import Message, Room
from django.contrib.auth.models import User

"""
    -   Nous essaierons d'afficher toute sorte d'objet au format json.
    -   La méthode get_object nous permet retourner l'objet recherché.
    -   La méthode get nous permet de récuper l'objet retourné par la méthode get_object et d'appliquer notre sérialisation.
"""


# Classe pour lister au format json tous les messages .
class MessagesListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Classe pour lister au format json tous les rooms (salles de chat).
class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Classe pour lister au format json les détails d'un objet de type message.
class MessageDetailView(APIView):

    def get_object(self, id):
        try:
            return Message.objects.get(id=id)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        message = self.get_object(id)
        serializer = MessageSerializer(message)
        return Response(serializer.data)


# Classe pour lister au format json les détails d'un objet de type room (salle de chat).
class RoomDetailView(APIView):

    def get_object(self, id):
        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        room = self.get_object(id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)


# Classe pour lister au format json tous les objets de type message d'un utilisateur.
class GetUserMessagesView(APIView):

    def get_object(self, user):
        try:
            user = User.objects.get(username=user)
        except Exception as e:
            raise e
        if user:
            try:
                return Message.objects.filter(user=user)
            except Exception as e:
                raise e

    def get(self, request, user, format=None):
        user_messages = self.get_object(user)
        serializer = MessageSerializer(user_messages, many=True)
        return Response(serializer.data)


# Classe pour lister au format json tous les objets de type room (salles de chat) d'un utilisateur.
class GetUserRoomsView(APIView):

    def get_object(self, user):
        try:
            user = User.objects.get(username=user)
        except Exception as e:
            raise e
        if user:
            try:
                user.landlord != None
                return Room.objects.filter(user1=user)
            except:
                user.client != None
                return Room.objects.filter(user2=user)

    def get(self, request, user, format=None):
        user_rooms = self.get_object(user)
        serializer = RoomSerializer(user_rooms, many=True)
        return Response(serializer.data)


# Classe pour lister au format json tous les objets de type message d'un utilisateur par room (salle de chat).
class GetUserRoomMessageView(APIView):

    def get_object(self, id, user):
        try:
            room = Room.objects.get(id=id)
            user = User.objects.get(username=user)
        except Exception as e:
            raise e
        if room and user:
            try:
                return Message.objects.filter(user=user, room=room)
            except Exception as e:
                raise e

    def get(self, request, id, user, format=None):
        user_room_messages = self.get_object(id, user)
        serializer = MessageSerializer(user_room_messages, many=True)
        return Response(serializer.data)


# Classe pour lister au format json les détails du dernier objet de type message d'un utilisateur par room (salle de chat).
class GetUserRoomLatestMessageView(APIView):

    def get_object(self, id, user):
        try:
            room = Room.objects.get(id=id)
            user = User.objects.get(username=user)
        except Exception as e:
            raise e
        if room and user:
            try:
                messages = Message.objects.filter(user=user, room=room)
                return messages.latest('id')
            except Exception as e:
                pass

    def get(self, request, id, user, format=None):
        user_room_messages = self.get_object(id, user)
        serializer = MessageSerializer(user_room_messages)
        return Response(serializer.data)
