from kivy.uix.gridlayout import GridLayout
import plane
from gamebutton import GameButton


class BattleShips(GridLayout):

    def __init__(self, **kwargs):
        super(BattleShips, self).__init__(**kwargs)
        # print('konstruktora BattleShips')

    def isShip(self, x, y):
        return self.ids['player'].ids[y].ids[y].isShip

    def onMessage(self, message):
        # print(__name__, '=>', message)
        print(' onMessage =>', message)
