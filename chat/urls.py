from django.urls import path , include
from . import views 
urlpatterns = [
     path('<str:room_name>/', views.chat_room, name='chat'),
]