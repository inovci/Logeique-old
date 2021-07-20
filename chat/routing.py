# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"^chat/(?P<username>[\w.@+-]+)/[0-9]$", consumers.ChatConsumer.as_asgi()),
]
