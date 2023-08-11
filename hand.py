class Hand:
    def __init__(self, soft_score: int, hard_score: int, cards: list):
        self.soft_score = soft_score
        self.hard_score = hard_score
        self.cards = cards
        return

    def add_card(self, card: int):
        self.cards.append(card)
        self.set_hard_score()
        self.set_soft_score()
        return

    def add_hidden_card(self):
        self.cards.append('*')
        self.set_hard_score()
        self.set_soft_score()
        return

    def set_hard_score(self):
        cleaned_cards = self.clean_hand()
        self.hard_score = sum(cleaned_cards)
        return

    def set_soft_score(self):
        cleaned_cards = self.clean_hand()
        soft_hand = [x if x != 11 else 1 for x in cleaned_cards]
        self.soft_score = sum(soft_hand)
        return

    def check_blackjack(self):
        if self.soft_score == 21 or self.hard_score == 21:
            return True
        return False

    def check_bust(self):
        if self.soft_score > 21 or self.hard_score > 21:
            return True
        return False

    def clean_hand(self):
        cleaned_cards = [x for x in self.cards if x != '*']
        return cleaned_cards




