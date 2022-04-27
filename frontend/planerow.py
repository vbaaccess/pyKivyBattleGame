from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import gamebutton


class PlaneRow(GridLayout):
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(PlaneRow, self).__init__(**kwargs)
