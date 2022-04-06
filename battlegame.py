from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import plane


class TheGame(GridLayout):

    def __init__(self, **kwargs):
        super(TheGame, self).__init__(**kwargs)


class BattleGameApp(App):

    def build(self):
        self.title = 'Battle Game'
        return TheGame()


if __name__ == '__main__':
    Config.read('config.ini')
    BattleGameApp().run()
