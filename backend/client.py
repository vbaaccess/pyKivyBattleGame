import json
import sys
import time
import asyncio
import websockets

from message.Message import BaseMessage, AttackMessage

print(f'sys.argv({len(sys.argv)}):', sys.argv)


def setURI():
    if len(sys.argv) > 1:
        client_name = str(sys.argv[1])
    else:
        client_name = input('Enter client name:')

    sleep_time = 1
    if len(sys.argv) > 2:
        sleep_time = int(sys.argv[2])

    print(f' Start client {client_name} ({sleep_time})')
    # adess websocket'owy , ws -> protokol web sockets
    server_name = 'localhost'
    server_port = 8765
    uri = 'ws://' + server_name + ':' + str(server_port)
    return uri, client_name, sleep_time


def handleAttack(msg: AttackMessage):
    print("I've been hit", msg.x, msg.y, "!")


async def hello():
    uri, client_name, sleep_time = setURI()
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                now = time.strftime("%X")
                message_to_send = f"{client_name}: Hello ^_^ ({now})"
                print('Sending:', message_to_send)
                await websocket.send(message_to_send)
                msg_from_server = await websocket.recv()
                print('Received from server:', msg_from_server)
                # json.load => zamiana str na slownik (dict)
                msg_from_server = BaseMessage(data=json.load(msg_from_server))  # convert string to dict
                if msg_from_server.type == BaseMessage.PLAYER_DISCONNECTED:
                    print(BaseMessage.PLAYER_DISCONNECTED)
                    await websocket.close()
                    break
                elif msg_from_server.type == BaseMessage.ATTACK:
                    handleAttack(msg_from_server)
                await asyncio.sleep(sleep_time)
        except websockets.exceptions.ConnectionClosed as ex:
            print(ex)


asyncio.get_event_loop().run_until_complete(hello())
