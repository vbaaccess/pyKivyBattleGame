from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from gamebutton import GameButton

import plane

class BattleShips(GridLayout):

    isGameStarted = False

    def __init__(self, **kwargs):
        super(BattleShips, self).__init__(**kwargs)
        print('constructor BattleShips')
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


    def onMessage(self, message):
        print(' onMessage =>', message)  # receive message from server
        x = str(message['x'])
        y = str(message['y'])
        if self.isShip(x, y):
            self.ids['opponent'].ids[y].ids[x].hit()
        else:
            self.ids['opponent'].ids[y].ids[x].miss()

    def sendMessage(self, message):
        if not self.isGameStarted:
            return
        print(' sendMessage =>', message)   # send message to server
        self.onMessage(message)

    def isShip(self, x: str, y: str):
        return self.ids['player'].ids[y].ids[x].isShip


class BattleShipsApp(App):

    def build(self):
        return BattleShips()

if __name__ == '__main__':
    Config.read('config.ini')
    BattleShipsApp().run()
