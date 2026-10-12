from channels.generic.websocket import WebsocketConsumer

class EchoWebSocketConsumer(WebsocketConsumer):
    def websocket_connect(self):
        return self.accept()
    
        # return self.close()

    def receive(self, text_data = None, bytes_data = None):
        return super().receive(text_data, bytes_data)