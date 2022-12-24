from unittest import TestCase
from hand import Hand


class TestHand(TestCase):
    def setUp(self):
        self.hand = Hand(soft_score=0, hard_score=0, cards=[])


class TestInit(TestHand):
    def test_init_soft_score(self):
        self.assertEqual(self.hand.soft_score, 0)

    def test_init_hard_score(self):
        self.assertEqual(self.hand.hard_score, 0)

    def test_card_type(self):
        self.assertIsInstance(self.hand.cards, list)


class TestCards(TestHand):

    def test_add_single_card(self):
        self.hand.add_card(4)
        self.assertEqual(self.hand.cards, [4])

    def test_add_multiple_cards(self):
        self.hand.add_card(4)
        self.hand.add_card(8)
        self.assertEqual(self.hand.cards, [4, 8])


class TestScore(TestHand):

    def test_soft_score_change(self):
        self.hand.soft_score = 4
        self.assertEqual(self.hand.soft_score, 4)

    def test_hard_score_change(self):
        self.hand.hard_score = 4
        self.assertEqual(self.hand.hard_score, 4)

    def test_check_blackjack(self):
        self.hand.add_card(10)
        self.hand.add_card(11)
        self.assertTrue(self.hand.check_blackjack())

    def test_clean_hand(self):
        self.fail()

    def test_print_hand_info(self):
        self.fail()
