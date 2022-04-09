from kivy.uix.gridlayout import GridLayout
import plane
from gamebutton import GameButton


class BattleShips(GridLayout):

    def __init__(self, **kwargs):
        super(BattleShips, self).__init__(**kwargs)
        print('konstruktora BattleShips')
                            # kv <BattleShips>

        # print('self.children', self.children)
        for c1 in self.children:
            print(type(c1))
        # for kv_GridLayout in self.children:                                  # 1
        #     print(type(kv_GridLayout))
        #     for kv_GridLayout_Plane_id in kv_GridLayout.children:       # 2 player and opponent
        #         print(type(kv_GridLayout_Plane_id))
        #         for kv_Plane in kv_GridLayout_Plane_id.children:        # 3
        #             # print(type(kv_Plane))
        #             for kv_Obj in kv_Plane.children:                    # 4
        #                 print(type(kv_Obj))
        #                 if isinstance(kv_Obj, GameButton):
        #                     kv_Obj.sendMessage = self.sendMessage
        #                     # pass

    def isShip(self, x, y):
        return self.ids['player'].ids[y].ids[y].isShip

    def onMessage(self, message):
        # print(__name__, '=>', message)
        print(' onMessage =>', message)

    def sendMessage(self, message):
        # print(__name__, '=>', message)
        print(' sendMessage =>', message)
