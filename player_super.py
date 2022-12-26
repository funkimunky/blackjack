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
        # params = {'isBust': False, 'isBlackjack': False}
        # if check_bust(hand):
        #     params['isBust'] = True
        #     return params
        #
        # if check_blackjack(hand):
        #     params['isBlackjack'] = True
        #     return params
        #
        # return params
        return