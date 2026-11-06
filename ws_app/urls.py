from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('timer/start/', views.timer_start, name='timer_start'),
    path('timer/view/<str:room_name>/', views.timer_view, name='timer_view'),
    path('send-msg/', views.send_message, name='send_message'),
]