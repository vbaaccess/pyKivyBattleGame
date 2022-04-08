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
        if self.isShip:
            self.background_color = (0, 0.9, 0)
        else:
            self.background_color = (0.1, 0.5, 0.6, 1) # blue see
