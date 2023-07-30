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
        self.game.add_dealer(Dealer('Dave', Hand(0, 0, [])))
        self.game.add_player(Player('Bob', Hand(0, 0, [])))
        self.game.add_player(Player('Alice', Hand(0, 0, [])))
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
        self.assertEqual(dealer.name, "Dave")

    def test_add_player_type(self):
        for player in self.game.players:
            self.assertIsInstance(player, Player)

    def test_deal_card(self):
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




