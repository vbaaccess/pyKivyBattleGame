from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from gamebutton import GameButton

import plane

class BattleShips(GridLayout):

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

        print("Click Button START")

    def onMessage(self, message):
        pass

    def sendMessage(self, message):
        print(' sendMessage =>', message)   # send message to server

    def isShip(self, x, y):
        return self.ids['player'].ids[y].ids[x].isShip


class BattleShipsApp(App):

    def build(self):
        return BattleShips()

if __name__ == '__main__':
    Config.read('config.ini')
    BattleShipsApp().run()
