import asyncio
import threading
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
from asyncio import sleep


class WSConsumer(AsyncWebsocketConsumer):

    async def run_generating(self):
        while True:
            numbers.append(random.randint(1, 1000))
            await sleep(5)

    def start_generating_loop(self):
        policy = asyncio.get_event_loop_policy()
        policy.set_event_loop(policy.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(self.run_generating()))

    async def send_number(self, wait=True):
        await self.send(json.dumps({'message': numbers[-1] if len(numbers) != 0 else 0}))
        await sleep(5 if wait else 0)

    async def connect(self):
        global numbers
        await self.accept()
        if len(numbers) == 0:
            thread = threading.Thread(target=self.start_generating_loop)
            thread.start()
            while True:
                if len(numbers) != 0:
                    await self.send_number()
        await self.send_number(wait=False)
        current_number = numbers[-1]
        while numbers[-1] == current_number:
            await sleep(0.1)
        while True:
            await self.send_number()


numbers = []
