from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
	path('user/<int:user1_id>/user/<int:user2_id>', views.checkview, name='checkview'),
	path('send/<int:user_id>/<int:room_id>' , views.send , name = 'send')
]