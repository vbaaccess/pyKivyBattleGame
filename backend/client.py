import sys
import time
import asyncio
import websockets

print(f'sys.argv({len(sys.argv)}):', sys.argv)


async def hello():
    if len(sys.argv) > 1:
        client_name = str(sys.argv[1])
    else:
        client_name = input('Enter client name:')

    sleep_time = 1
    if len(sys.argv) > 2:
        sleep_time = int(sys.argv[2])

    print(f' Start client {client_name} ({sleep_time})')
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
            await asyncio.sleep(sleep_time)

asyncio.get_event_loop().run_until_complete(hello())
