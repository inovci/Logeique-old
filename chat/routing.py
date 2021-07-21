# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    #re_path(r"chat/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/$", consumers.ChatConsumer.as_asgi()),
    path("chat/room/<int:room_id>", consumers.ChatConsumer.as_asgi()),
    #path("chat/<str:user2>/<str:user1>", consumers.ChatConsumer.as_asgi()),
]
