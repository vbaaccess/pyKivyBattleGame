class Game:
    players = []

    def __init__(self):
        self.players = []

    def add_player(self, websocket):
        self.players.append(websocket)

    async def handle(self, websocket, message):
        pass

    async def sendToOther(self, websocket, message):
        pass
