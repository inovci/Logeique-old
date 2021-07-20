# chat/consumers.py
import json
import asyncio
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        print("Connected !!!", event)
        """
        other_user = self.scope['url_route']['kwargs']
        user = self.scope['user']
        print(other_user, user)
        room_obj = await self.get_thread(user, other_user)
        self.room_obj = room_obj

        chat_room = f"room_{room_obj.id}"
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        """
        await self.accept()

    async def websocket_receive(self, text_data):
        # When a message is received from the websocket
        print("Receive !!!", text_data)
        front_text = text_data.get("text", None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            print(msg)
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
    def get_thread(self, user, other_user):
        return Room.objects.get_or_new(user, other_user)[0]

    @database_sync_to_async
    def creat_chat_message(self, user, msg):
        room_obj = self.room_obj
        return ChatMessage.objects.create(room=room_obj, user=user, message=msg)


class ChatConsumerTuto(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
