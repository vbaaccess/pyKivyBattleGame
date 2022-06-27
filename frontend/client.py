import asyncio


class Client:

    def __init__(self):
        self._stop = False

    async def run(self):
        while not self._stop:
            await asyncio.gather(
                self.send(),
                self.receive()
            )

    async def send(self):
        while not self._stop:
            print("Send (TEST)")
            await asyncio.sleep(5)

    async def receive(self):
        while not self._stop:
            print("Receive (TEST)")
            await asyncio.sleep(5)

    def stop(self):
        self._stop = True
