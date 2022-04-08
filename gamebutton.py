import constant.colors as cc
from kivy.properties import BooleanProperty, DictProperty
from kivy.uix.button import Button


class GameButton(Button):
    coordinate = DictProperty({"x": 0, "y": 0})
    isShip = BooleanProperty(False)
    wasHit = BooleanProperty(False)

    def on_release(self):
        super(GameButton, self).on_release()
        self.isShip = not self.isShip
        self.updateColor()
        print(self.coordinate)

    def updateColor(self):
        bg_color = cc.BLUE_SEE

        if self.isShip:
            bg_color = cc.DARK_GREEN

        self.background_color = bg_color
