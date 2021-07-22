# chat/consumers.py
import json
import asyncio
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        print("Connected !!!", event)

        user = self.scope['user']
        room = self.scope['url_route']['kwargs']
        room_id = room['room_id']

        room_obj = await self.get_room(room_id)
        print(room_obj)

        self.room_obj = room_obj

        chat_room = f"room_{room_obj.id}"
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        await self.accept()

    async def websocket_receive(self, text_data):
        # When a message is received from the websocket
        print("Receive !!!", text_data)
        front_text = text_data.get("text", None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            user = self.scope['user']
            username = 'default_user'
            if user.is_authenticated:
                username = user.username
            myResponse = {
                "message": msg,
                "username": username
            }
            await self.creat_chat_message(user, msg)

            new_event = {
                "type": "chat_message",
                "data": json.dumps(myResponse)
            }
            #await self.send(text_data=json.dumps(myResponse))

            await self.channel_layer.group_send(
                self.chat_room,
                new_event
            )

    async def chat_message(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=data)



    async def disconnect(self, close_code):
        # When the socket connects
        print("Disconnected !!!")


    # My own methods
    @database_sync_to_async
    def get_room(self, room_id):
        return get_object_or_404(Room, id=room_id)

    @database_sync_to_async
    def creat_chat_message(self, user, msg):
        room_obj = self.room_obj
        return Message.objects.create(room=room_obj, user=user, value=msg)
