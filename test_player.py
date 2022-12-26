from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from player import Player
from hand import Hand


class TestPlayer(TestCase):
    def setUp(self):
        self.hand = Hand(soft_score=0, hard_score=0, cards=[])
        self.player = Player("David", self.hand)


class TestInit(TestPlayer):
    def test_type(self):
        self.assertIsInstance(self.player, Player)


class TestParameters(TestPlayer):
    def test_name(self):
        self.assertEqual(self.player.name, "David")

    def test_hand_type(self):
        self.assertIsInstance(self.player.hand, Hand)


class TestMethods(TestPlayer):

    @patch('sys.stdout', new_callable=StringIO)
    def test_printing_hand(self, mock_stdout):
        self.player.hand.add_card(9)
        self.player.hand.add_card(11)
        self.player.print_hand_info()
        self.assertEqual("""David's hand\n[9, 11]\nhard score:20\nsoft score:10\n""", mock_stdout.getvalue())
        # assert mock_stdout.getvalue() == "David's hand \n[9, 11]\nhard score:20\nsoft score:10\n" # does not give comparison


