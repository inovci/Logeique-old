from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
<<<<<<< HEAD
    path('<str:room_name>/', views.room, name='room'),
]

urlpatterns = [
	path('landlord/<int:user1_id>/client/<int:user2_id>', views.landlordCheckview, name='landlordCheckview'),
	path('client/<int:user1_id>/landlord/<int:user2_id>', views.clientCheckview, name='clientCheckview'),

	#path('send/<int:user_id>/<int:room_id>', views.send, name='send'),
	#path('receive/<int:room_id>' , views.receive , name = 'receive')

]
=======
	path('<str:other_user>', views.checkview, name='checkview'),
	#path('<str:user1>/<str:user2>', views.clientCheckview, name='clientCheckview'),
	path('send/<int:user_id>/<int:room_id>', views.send, name='send'),
	path('room/<int:room_id>', views.room, name='room'),
	path('receive/<int:room_id>' , views.receive , name = 'receive'),
	#re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]
>>>>>>> c7c71191ba4855a676a38f4b040062d955ea9d73
