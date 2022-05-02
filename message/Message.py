class BaseMessage:
    """
    Base class specifying the type of message
    """
    PLAYER_DISCONNECTED = "PLAYER_DISCONNECTED"
    PLAYER_CONNECTED = "PLAYER_CONNECTED"
    HIT = "ATTACK"
    HIT = "HIT"
    MISS = "MISS"
    SANK = "SANK"

    def __init__(self):
        pass
