from django.urls import path
from .views import main, send_message

urlpatterns = [
    path('', main),
    path('send', send_message)
]