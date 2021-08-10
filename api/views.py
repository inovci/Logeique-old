from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.views import APIView

from .serializers import MessageSerializer
from chat.models import Message
from django.contrib.auth.models import User


class MessagesListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


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
