import json


class BaseMessage:
    """
    Base class specifying the type of message
    It stores basic information about the message:
    - message type,
    """
    NULL = "NULL"
    PLAYER_DISCONNECTED = "PLAYER_DISCONNECTED"
    PLAYER_CONNECTED = "PLAYER_CONNECTED"
    ATTACK = "ATTACK"
    HIT = "HIT"
    MISS = "MISS"
    SANK = "SANK"
    GAME_ID_NOT_ALLOWED = "GAME_ID_NOT_ALLOWED"
    YOU_WON = "YOU_WON"

    def __init_subclass__(cls, **kwargs):
        # --- STEP 0 --- only in subclass
        BaseMessage.__init__(cls)

    def __init__(self, date=None):
        # --- STEP 1 ---
        self.type = self.NULL
        if date is not None:
            self.__dict__ = date

    def toJSON(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)


class PlayerDisconnectedMessage(BaseMessage):
    def __init__(self):
        self.type = self.PLAYER_DISCONNECTED


class PlayerConnectedMessage(BaseMessage):
    def __init__(self):
        self.type = self.PLAYER_CONNECTED


class AttackMessage(BaseMessage):
    def __init__(self, x=0, y=0):
        self.type = self.ATTACK
        self.x = x
        self.y = y


class HitMessage(BaseMessage):
    def __init__(self):
        self.type = self.HIT


class MissMessage(BaseMessage):
    def __init__(self):
        self.type = self.MISS


class SankMessage(BaseMessage):
    def __init__(self):
        self.type = self.SANK
