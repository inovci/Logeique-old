from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('<str:other_user>', views.checkview, name='checkview'),
	path('room/<int:room_id>', views.room, name='room'),
]
