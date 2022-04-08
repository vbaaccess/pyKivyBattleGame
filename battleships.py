from kivy.uix.gridlayout import GridLayout
import plane


class BattleShips(GridLayout):

    def isShip(self, x, y):
        return self.ids['player'].ids[y].ids[y].isShip
