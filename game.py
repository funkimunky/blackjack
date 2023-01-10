import random

from player_super import PlayerSuper
from dealer import Dealer
from hand import Hand
from art import logo


class Game:
    def __init__(self):
        self.player = []
        self.dealer = []
        self.play_again = True
        self.logo = logo
        self.card_possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return

    def add_dealer(self, dealer: PlayerSuper):
        self.dealer.append(dealer)
        return

    def add_player(self, player: PlayerSuper):
        self.player.append(player)
        return

    def deal_card(self, player: PlayerSuper):
        player.hand.add_card(random.choice(self.card_possibles))
        return

    def choose_hit_or_stand(self, player: PlayerSuper):
        while True:  # Never ending loop
            try:
                decision = str(input(f'Hit (h) or Stand (s)?/n'))
                if decision.lower() == 'h' or decision.lower() == 's':
                    break
                else:
                    raise TypeError
            except TypeError:
                print("invalid input./n")
                continue  # This causes it to continue
            except EOFError:
                print("Please input something....")
                continue  # This causes it to continue

        return

    def display_start(self):
        return

    def display_end(self):
        return

    def ask_play_again(self):
        return

    def display_winner(self):
        return

    def game_loop(self):
        return


