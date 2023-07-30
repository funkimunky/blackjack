from player_super import PlayerSuper
from hand import Hand


class Dealer(PlayerSuper):
    def __init__(self, name: str):
        hand = Hand(0, 0, [])
        super().__init__(name, hand)
