from django.shortcuts import render
from django.http import HttpResponse
from channels.layers import get_channel_layer


def main(request):
    return render(request, 'code.html')


def timer_start(request):
    return render(request, 'start.html')


def timer_view(request, room_name):
    return render(request, 'timer.html', {'room_name': room_name})


async def send_message(request):
    message = request.GET.get('msg', '')
    layer = get_channel_layer()
    await layer.group_send(
        'messages',
        {'type': 'message.new', 'text': message}
    )
    return HttpResponse(status=204)