from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import battleships


class TheGame(GridLayout):

    def __init__(self, **kwargs):
        super(TheGame, self).__init__(**kwargs)
        # self.ids['opponent'].disabled = True

    def startButtonClick(self):
        # self.ids['oid_GridBattleShips'].ids['player'].disabled = True
        # self.ids['opponent'].disabled = False
        self.ids['oid_gameTextInput'].disabled = True
        self.ids['oid_gameStartButton'].disabled = True

        print("Click Button START")

class BattleGameApp(App):

    def build(self):
        self.title = 'Battle Game'
        return TheGame()


if __name__ == '__main__':
    Config.read('config.ini')
    BattleGameApp().run()
