from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('<int:house_id>', views.checkviewClient, name='checkviewClient'),
	path('<str:other_user>', views.checkviewLandlord, name='checkviewLandlord'),
	path('room/<int:room_id>', views.room, name='room'),
]
