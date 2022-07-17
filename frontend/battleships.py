import asyncio

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from frontend.client import Client
from gamebutton import GameButton

from message import Message

import plane


class BattleShips(GridLayout):


    def __init__(self, **kwargs):
        super(BattleShips, self).__init__(**kwargs)
        print('constructor BattleShips')
        self.isGameStarted = False
        self.client = Client(self.onMessage)
        self.ids['opponent'].disabled = True

        for c1 in self.children:
            for c2 in c1.children:
                for c3 in c2.children:
                    for c4 in c3.children:
                        if isinstance(c4, GameButton):
                            c4.sendMessage = self.sendMessage

    def startButtonClick(self):
        self.ids['player'].disabled = True
        self.ids['opponent'].disabled = False

        self.ids['oid_gameTextInput'].disabled = True
        self.ids['oid_gameStartButton'].disabled = True

        self.isGameStarted = True

        print("Click Button START")

    def onMessage(self, message: Message.BaseMessage):
        if message.type == Message.BaseMessage.ATTACK:
            print(' onMessage =>', message)  # receive message from server
            # x = int(message['x'])
            # y = int(message['y'])
            x = message.x
            y = message.y
            self.ids['player'].ids[str(y)].ids[str(x)].setWasHit()

            if self.isShip(x, y) and self.isSunken(x, y, {}):
                self.sank(x, y, {})
                self.sendMessage(Message.SankMessage())
            elif self.isShip(x, y):
                self.sendMessage(Message.HitMessage())
            else:
                self.sendMessage(Message.MissMessage())
        elif message.type == Message.BaseMessage.SANK:
            self.sank(x, y, {})
        elif message.type == Message.BaseMessage.HIT:
            self.ids['opponent'].ids[str(y)].ids[str(x)].hit()
        elif message.type == Message.BaseMessage.MISS:
            self.ids['opponent'].ids[str(y)].ids[str(x)].miss()

            # if self.isShip(x, y) and self.isSunken(x, y, {}):
            #     self.sank(x, y, {})
            # elif self.isShip(x, y):
            #     self.ids['opponent'].ids[str(y)].ids[str(x)].hit()
            # else:
            #     self.ids['opponent'].ids[str(y)].ids[str(x)].miss()

    # def sendMessage(self, message):
    #     if not self.isGameStarted:
    #         return
    #     print(' sendMessage =>', message)   # send message to server
    #     self.onMessage(message)

    def sendMessage(self, message):
        if not self.isGameStarted:
            return
        self.client.sendMessage(message)

    def wasHit(self, x: int, y: int):
        return self.ids['player'].ids[str(y)].ids[str(x)].wasHit

    def isShip(self, x: int, y: int):
        return self.ids['player'].ids[str(y)].ids[str(x)].isShip

    # visited: for the purpose of checkin that the entire ship has been sunk
    def isSunken(self, x, y, visited):
        if not self.isShip(x, y):
            return False

        if (x, y) not in visited:
            if self.wasHit(x, y):
                visited[(x, y)] = True

                # --- moore Neighborhood -------------------------------------------
                # https://en.wikipedia.org/wiki/Moore_neighborhood
                for i in range(y-1, y+2):
                    if i == 0 or i == 11:
                        continue
                    for j in range(x-1, x+2):
                        if j == 0 or j == 11 or (i == y and j ==x):
                            continue
                        if self.isShip(j, i) and not self.isSunken(j, i, visited):
                            return False
                # -------------------------------------------------------------------
            else:
                return False

        return True

    def sank(self, x, y, visited):
        if (x, y) not in visited:
            visited[(x, y)] = True
            for i in range(y-1, y+2):
                if i == 0 or i == 11:
                    continue
                for j in range(x-1, x+2):
                    if j == 0 or j == 11:
                        continue
                    self.ids['player'].ids[str(y)].ids[str(x)].setWasHit()
                    self.ids['opponent'].ids[str(y)].ids[str(x)].setWasHit()
                    if self.ids['opponent'].ids[str(y)].ids[str(x)].isShip:
                        self.sank(j, i, visited)


class BattleShipsApp(App):

    # def build(self):
    #     return BattleShips()

    async def async_run(self, async_lib=None):
        self.load_config()
        self.load_kv(filename=self.kv_file)
        self.root = BattleShips()
        await asyncio.gather(
            super(BattleShipsApp, self).async_run(async_lib=async_lib),
            self.root.client.run()
        )

    def stop(self):
        self.root.client.stop()
        super(BattleShipsApp, self).stop()
