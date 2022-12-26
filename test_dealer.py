from unittest import TestCase
from dealer import Dealer


class TestDealer(TestCase):
    def setUp(self):
        self.dealer = Dealer("Jack", [])


class TestInit(TestDealer):
    def test_type(self):
        self.assertIsInstance(self.dealer, Dealer)


class TestParameters(TestDealer):
    def test_name(self):
        self.assertEqual(self.dealer.name, "Jack")

    def test_hand_type(self):
        self.assertIsInstance(self.dealer.hand, list)
