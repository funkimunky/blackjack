from hand import Hand
from game import Game
from player import Player
from dealer import Dealer
from hand import Hand
def start_game():
    game = Game()
    game.display_start()
    dealer = game.add_dealer("John")
    david = game.add_player("David")
    # bob = game.add_player("Bob")
    # bob = game.get_player("Bob")
    # bob.name = "test"
    game.deal_card(david)
    return

# def play_loop(player):
#     global player_hand, dealer_hand, player_score, dealer_score
#     twist = 'y'
#     while twist == 'y':
#         my_hand = check_hand(player_hand)
#
#         if my_hand['isBust']:
#             print(f'You lose')
#
#         if my_hand['isBlackjack']:
#             print(f'You win')
#
#         twist = input("twist? y/n \n").lower()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()
    # play_loop('player')