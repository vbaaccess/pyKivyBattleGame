import json
import time

from message.Message import PlayerDisconnectedMessage, BaseMessage
# from message import Message


class Game:
    lastActivity = time.time()
    players = []

    def __init__(self):
        self.players = []
        self.lastActivity = time.time()

    def add_player(self, websocket):
        self.players.append(websocket)

    async def handle(self, websocket, message):
        self.lastActivity = time.time()
        if len(self.players) == 2:
            message = BaseMessage(date=json.loads(message))  # convert string to dict
            if message.type == BaseMessage.PLAYER_DISCONNECTED:
                await self.sendToBoth(message.toJSON())
            else:
                await self.sendToOther(websocket, message.toJSON())

    async def sendToOther(self, websocket, message):
        # wyslanie wiadomosci do wszystkich klientow z wylaczeniem nadawcy
        # wpis: rozsylam otrzymana wiadomosc do pozostalych
        #   klucz
        # if len(self.player) > 1:
        #     print('Forwarding the message:')

        # player = > client websocket
        for player in self.players:
            if player == websocket:
                continue
            # print(f' to {player}: ', message)
            await player.send(message)

    async def sendToBoth(self, message):
        for player in self.players:
            await player.send(message)

    async def timeout(self):
        # send message to all players
        for player in self.players:
            await player.send("Timeout")

    async def handleDisconnect(self, websocket):
        if self.players == 1:
            return
        await self.sendToOther(websocket, PlayerDisconnectedMessage().toJSON())
        if self.players[0] == websocket:
            del self.players[0]
        else:
            del self.players[1]
