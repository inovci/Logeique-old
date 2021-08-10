from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('messages/', MessagesListView.as_view()),
    path('messages/<int:id>/', MessageDetailView.as_view()),
    path('messages/<str:user>/', GetUserMessagesView.as_view()),
]