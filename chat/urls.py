from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('<str:other_user>', views.checkview, name='checkview'),
	#path('<str:user1>/<str:user2>', views.clientCheckview, name='clientCheckview'),
	path('send/<int:user_id>/<int:room_id>', views.send, name='send'),
	path('room/<int:room_id>', views.room, name='room'),
	path('receive/<int:room_id>' , views.receive , name = 'receive'),
	#re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]