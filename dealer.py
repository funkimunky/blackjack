from player_super import PlayerSuper

class Dealer(PlayerSuper):
    def __init__(self, name: str, hand: list):
        self.name = name
        self.hand = hand
