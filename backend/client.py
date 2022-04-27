import time
import asyncio
import websockets


async def hello():
    client_name = input('Enter client name:')
    # adess websocket'owy , ws -> protokól web sockets
    server_name = 'localhost'
    server_port = 8765
    uri = 'ws://' + server_name + ':' + str(server_port)
    async with websockets.connect(uri) as websocket:
        while True:
            now = time.strftime("%X")
            message_to_send = f"{client_name}: Hello ^_^ ({now})"
            print('Sending:', message_to_send)
            await websocket.send(message_to_send)
            msg_from_server = await websocket.recv()
            print('Received from server:', msg_from_server)
            await asyncio.sleep(5)

asyncio.get_event_loop().run_until_complete(hello())
