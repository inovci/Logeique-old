from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('<int:house_id>', views.checkviewClient, name='checkviewClient'),
	path('<str:other_user>-<int:proposal_id>', views.checkviewLandlord, name='checkviewLandlord'),
	path('room/<int:room_id>', views.room, name='room'),
	path('room/<int:lanlord_id>-<int:client_id>-<int:house_id>/' , views.concluded_deal , name='concluded_deal')
]
