# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)


import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Close the WebSocket connection
        await self.close()

    async def receive(self, text_data):
        # Parse the received JSON data
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Broadcast the received message to all clients in the same group
        await self.channel_layer.group_add('task_status_group', self.channel_name)
        await self.channel_layer.group_send(
            'task_status_group',
            {
                'type': 'chat.message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))


    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)

    #     message = text_data_json.get('message')

    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))


    # async def receive(self, text_data):
    #     try:
    #         data = json.loads(text_data)
    #         logger.info(f"Received WebSocket data: {data}")
            
    #         # Handle the received data here

    #     except json.JSONDecodeError as e:
    #         logger.error(f"Failed to decode JSON: {e}")