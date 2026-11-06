from channels.routing import URLRouter
from django.urls import path
from .consumer import EchoConsumer, TimerConsumer

router = URLRouter([
    path('ws/echo', EchoConsumer.as_asgi()),
    path('ws/timer/<str:room_name>', TimerConsumer.as_asgi()),
])