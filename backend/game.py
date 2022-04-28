class Game:
    players = []

    def __init__(self):
        self.players = []

    def add_player(self, websocket):
        self.players.append(websocket)

    async def handle(self, websocket, message):
        self.sendToOther(websocket, message)

    async def sendToOther(self, websocket, message):
        # player = > client websocket
        for player in self.players:
            if player == websocket:
                continue
            print(f' to {player}: ', message)
            await player.send(message)

    async def sendToAll(self, websocket, message):
        pass
