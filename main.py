from kivy import Config
from battleships import BattleShipsApp

if __name__ == '__main__':
    Config.read('config.ini')
    BattleShipsApp().run()