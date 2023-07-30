from hand import Hand


class PlayerSuper:
    def __init__(self, name: str, hand: Hand):
        self.name = name
        self.hand = hand

    def print_hand_info(self):
        print(f'{self.name}\'s hand'
              f'\n{self.hand.cards}'
              f'\nhard score:{self.hand.hard_score}'
              f'\nsoft score:{self.hand.soft_score}')
        return

    def check_hand(self):
        self.hand.check_blackjack()
        self.hand.check_bust()
        return
