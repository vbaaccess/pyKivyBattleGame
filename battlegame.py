from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import battleships
from gamebutton import GameButton


class TheGame(GridLayout):

    def __init__(self, **kwargs):
        super(TheGame, self).__init__(**kwargs)
        # self.ids['opponent'].disabled = True

        # for obj_battleships in self.children[1].children[0].children:
        #     print(type(obj_battleships))

        for c1 in self.children:
            for c2 in c1.children:
                for c3 in c2.children:
                    for c4 in c3.children:
                        for c5 in c4.children:
                            if isinstance(c5, GameButton):
                                c5.sendMessage = self.sendMessage

    def startButtonClick(self):
        # self.ids['oid_GridBattleShips'].ids['player'].disabled = True
        # self.ids['opponent'].disabled = False
        self.ids['oid_gameTextInput'].disabled = True
        self.ids['oid_gameStartButton'].disabled = True

        print("Click Button START")

    def sendMessage(self, message):
        # print(__name__, '=>', message)
        print(' sendMessage =>', message)

class BattleGameApp(App):

    def build(self):
        self.title = 'Battle Game'
        return TheGame()


if __name__ == '__main__':
    Config.read('config.ini')
    BattleGameApp().run()
