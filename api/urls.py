from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    # For Messages
    path('messages/', MessagesListView.as_view()),
    path('messages/<int:id>/', MessageDetailView.as_view()),
    path('messages/<str:user>/', GetUserMessagesView.as_view()),
    # For Rooms
    path('rooms/', RoomListView.as_view()),
    path('rooms/<int:id>/', RoomDetailView.as_view()),
    path('rooms/<str:user>/', GetUserRoomsView.as_view()),
]