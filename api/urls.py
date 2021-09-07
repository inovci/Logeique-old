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
    # For Room Messages
    path('rooms/room-messages/<int:id>/', RoomMessagesView.as_view()),
    path('rooms/room-last-message/<int:id>/', RoomLatestMessageView.as_view()),
    path('rooms/messages/<int:id>/<str:user>/', GetUserRoomMessageView.as_view()),
    path('rooms/messages/latest/<int:id>/<str:user>/', GetUserRoomLatestMessageView.as_view()),
    # For Deal
    path('deals/', DealListView.as_view()),
    path('deals/<int:id>/', DealDetailView.as_view()),
]