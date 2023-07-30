import random
from player_super import PlayerSuper
from player import Player
from dealer import Dealer
from dealer import Dealer
from hand import Hand
from art import *


class Game:
    def __init__(self):
        self.players = []
        self.dealers = []
        self.play_again = True
        self.logo = logo
        self.card_possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return

    def add_dealer(self, name):
        new_dealer = Dealer(name)
        self.dealers.append(new_dealer)
        return new_dealer

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)
        return new_player

    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

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
        print(self.logo)
        return

    def display_end(self):
        return

    def ask_play_again(self):
        return

    def display_winner(self):
        return

    def game_loop(self):
        return


