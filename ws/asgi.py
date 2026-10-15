"""
ASGI config for ws project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from ws_app.websocket_routing import router 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws.settings')

# router = URLRouter(
#     [
#         path('ws/echo', EchoWebsocketConsumer.as_asgi())
#     ]
# )
django_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_app,
        'websocket': router
    }
)

#install django, uvicorn, channels