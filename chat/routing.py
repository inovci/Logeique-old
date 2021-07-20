# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    #re_path(r"chat/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/(?P<username>[\w.@+-]+)/$", consumers.ChatConsumer.as_asgi()),
    path("chat/landlord/<str:user1>/client/<str:user2>", consumers.ChatConsumer.as_asgi()),
]
