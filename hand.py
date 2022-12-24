class Hand:
    def __init__(self, soft_score: int, hard_score: int, cards: list):
        self.soft_score = soft_score
        self.hard_score = hard_score
        self.cards = cards

    def add_card(self, card: int):
        self.cards.append(card)
        return


    def check_score(self):
        if (11 in self._cards):
            score['softscore'] = self.get_soft_score()
            score['hardscore'] = get_hard_score()
        else:
            score['hardscore'] = sum(hand)

        return score

    def check_bust(self):
        # soft_score = 0
        #
        # if 11 in hand:
        #     soft_score = get_soft_score(hand)
        #
        # hard_score = get_hard_score(hand)
        #
        # if soft_score > 21 or hard_score > 21:
        #     return True
        #
        # return False
        return


    def check_blackjack(self):
        soft_score = 0

        if 11 in hand:
            soft_score = get_soft_score(hand)

        hard_score = get_hard_score(hand)

        if soft_score == 21 or hard_score == 21:
            return True

        return False



    def clean_hand(self):
        # cleaned_hand = [x for x in hand if x != '*']
        # return cleaned_hand
        return

    def print_hand_info(hand, name):
        # cleaned_hand = clean_hand(hand)
        # print(f'{name}\'s hand \n{hand}\nscore:{get_score(cleaned_hand)}')
        return
