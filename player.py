from player_super import PlayerSuper


class Player(PlayerSuper):
    def __init__(self, name: str, hand: list):
        super().__init__(name, hand)
