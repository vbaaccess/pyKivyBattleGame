import asyncio
import websockets


class Client:

    def __init__(self):
        self._stop = False
        self.messages = []

    async def run(self):
        while not self._stop:
            uri = "ws://loclahost:8765"
            async with websockets.connect(uri) as websocket:
                await asyncio.gather(
                    self.send(websocket),
                    self.receive(websocket)
                )

    def sendMessage(self, message):
        self.messages.append(message)

    async def send(self, websocket):
        while not self._stop or len(self.messages) > 0:
            if len(self.messages) == 0:
                await asyncio.sleep(0.1)
                continue
            message = self.messages.pop().toJSON()
            print("Sending:". message)
            # await asyncio.sleep(5)
            await websocket.send(message)

    async def receive(self, websocket):
        while not self._stop:
            message = await websocket.recv()
            print("Receive:", message)

    def stop(self):
        self._stop = True
