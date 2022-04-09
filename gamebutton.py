import constant.colors as cc
from kivy.properties import BooleanProperty, DictProperty, ObjectProperty
from kivy.uix.button import Button


class GameButton(Button):
    coordinate = DictProperty({"x": 0, "y": 0})
    isShip = BooleanProperty(False)
    wasHit = BooleanProperty(False)
    sendMessage = ObjectProperty()

    def on_release(self):
        super(GameButton, self).on_release()
        self.isShip = not self.isShip
        self.updateColor()
        print('on_release.coordinate', self.coordinate)
        self.sendMessage(self.coordinate)

    def hits(self):
        self.isShip = True
        self.wasHit = True

    def miss(self):
        self.isShip = False
        self.wasHit = True

    def updateColor(self):
        if self.isShip:
            if self.wasHit:
                bg_color = cc.RED
            else:
                bg_color = cc.DARK_GREEN
        else:
            if self.wasHit:
                bg_color = cc.DARK_BLUE_SEE
            else:
                bg_color = cc.BLUE_SEE

        self.background_color = bg_color
