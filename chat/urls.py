from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name='room'), #Dynamic url
    path('assessview', views.assessview, name='assessview'), # Url To assess the room being asked by user
    path('send', views.send, name='send'),  #In Line with our ajax "url", to add the functionality of sending the message
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),  #Get messages from a particular room (DYNAMIC URL)
]