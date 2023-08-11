from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from player import Player
from hand import Hand
from dealer import Dealer
from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add_dealer("John")
        self.game.add_player("Dave")
        self.game.add_player("Alice")
        self.game.card_possibles = [10]


class TestInit(TestGame):
    def test_type(self):
        self.assertIsInstance(self.game, Game)

    def test_player_type(self):
        self.assertIsInstance(self.game.players, list)

    def test_dealer_type(self):
        self.assertIsInstance(self.game.players, list)

    def test_play_again_type(self):
        self.assertIsInstance(self.game.play_again, bool)

    def test_logo_type(self):
        self.assertIsInstance(self.game.logo, str)


class TestSetupGame(TestGame):
    def test_add_dealer_type(self):
        for dealer in self.game.dealers:
            self.assertIsInstance(dealer, Dealer)

    def test_dealer_name(self):
        dealer = self.game.dealers[0]
        self.assertEqual(dealer.name, "John")

    def test_add_player_type(self):
        for player in self.game.players:
            self.assertIsInstance(player, Player)

    def test_player1_name(self):
        player = self.game.players[0]
        self.assertEqual(player.name, "Dave")

    def test_player2_name(self):
        player = self.game.players[1]
        self.assertEqual(player.name, "Alice")

    def test_get_player1ByName(self):
        player = self.game.get_player("Dave")
        self.assertEqual(player.name, "Dave")

    def test_get_player2ByName(self):
        player = self.game.get_player("Alice")
        self.assertEqual(player.name, "Alice")

    def test_deal_cardsDealer(self):
        dealer = self.game.dealers[0]
        self.game.deal_card(dealer, True)
        self.game.deal_card(dealer)
        self.assertEqual(dealer.hand.cards[0], "*")
        self.assertEqual(dealer.hand.cards[1], 10)

    def test_deal_cardsPlayer1(self):
        player = self.game.players[0]
        self.game.deal_card(player)
        self.assertEqual(player.hand.cards[0], 10)

    #https://deniscapeto.com/2021/03/06/how-to-test-a-while-true-in-python/
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='notright')
    def test_hit_stand(self, mock_input, mock_stdout):
        player = self.game.players[0]
        game = self.game
        self.game.choose_hit_or_stand(player)
        self.assertEqual('invalid input./n', mock_stdout.getvalue())




