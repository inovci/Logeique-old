from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('landlord/<str:user1>/client/<str:user2>', views.landlordCheckview, name='landlordCheckview'),
	path('client/<str:user1>/landlord/<str:user2>', views.clientCheckview, name='clientCheckview'),
	path('send/<int:user_id>/<int:room_id>', views.send, name='send'),
	path('receive/<int:room_id>' , views.receive , name = 'receive'),
	#re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]