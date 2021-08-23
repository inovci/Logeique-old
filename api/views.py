from django.core.checks import messages
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.views import APIView

from .serializers import MessageSerializer, RoomSerializer
from chat.models import Message, Room
from django.contrib.auth.models import User


class MessagesListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


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
