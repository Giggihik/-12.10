import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('messages', self.channel_name)
        await self.accept()

    async def disconnect(self, code: int) -> None:
        await self.channel_layer.group_discard('messages', self.channel_name)
        return await super().disconnect(code)

    async def message_new(self, event):
        await self.send(event['text'])


class TimerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'timer_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        self.task = None

    async def disconnect(self, code: int) -> None:
        if self.task:
            self.task.cancel()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        seconds = int(text_data or 0)
        if self.task:
            self.task.cancel()
        self.task = asyncio.create_task(self._countdown(seconds))

    async def _countdown(self, seconds):
        for remaining in range(seconds, -1, -1):
            await self.channel_layer.group_send(
                self.room_group_name, 
                {
                    'type': 'timer.tick',
                    'text': str(remaining),
                }
            )
            if remaining > 0:
                await asyncio.sleep(1)

    async def timer_tick(self, event):
        await self.send(text_data=event['text'])