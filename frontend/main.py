import asyncio

from kivy import Config
from battleships import BattleShipsApp

if __name__ == '__main__':
    Config.read('config.ini')
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        BattleShipsApp().async_run(async_lib='asyncio')
    )