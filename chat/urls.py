from django.urls import path, re_path
from . import views

app_name = "chat"

urlpatterns = [
	path('landlord/<int:user1_id>/client/<int:user2_id>', views.landlordCheckview, name='landlordCheckview'),
	path('client/<int:user1_id>/landlord/<int:user2_id>', views.clientCheckview, name='clientCheckview'),
	path('send/<int:user_id>/<int:room_id>', views.send, name='send'),
	path('receive/<int:room_id>' , views.receive , name = 'receive'),
	#re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]