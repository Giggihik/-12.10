from channels.generic.websocket import AsyncWebsocketConsumer
from uuid import UUID 
from random import randint
from asgiref.sync import sync_to_async
class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        session = self.scope['session']
        session['group'] = str(UUID())
        await sync_to_async(session.save)()
        self.channel_layer.group_add(
            'messages',
            self.channel_name
            )
        await self.accept()


    async def disconnect(self, code: int) -> None:
        await self.channel_layer.group_discard(
            'messages',
            self.channel_name
        )
        return await super().disconnect(code)


    
    # async def websocket_connect(self, message):
    #     return await self.accept()
    
        # return self.close()

    # async def receive(self, text_data = None, bytes_data = None):
    #     a, b = text_data.split('+')
    #     result =  float(a) + float(b)
    #     return await self.send(text_data=str(result))