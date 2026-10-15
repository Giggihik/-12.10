from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def websocket_connect(self, message):
        return await self.accept()
    
        # return self.close()

    async def receive(self, text_data = None, bytes_data = None):
        a, b = text_data.split('+')
        result =  float(a) + float(b)
        return await self.send(text_data=str(result))