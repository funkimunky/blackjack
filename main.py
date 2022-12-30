import random

import art

player_score = 0
dealer_score = 0
player_hand = []
dealer_hand = []
dealer_stand = 17
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 10]

def deal_card(hand: list):
    global cards
    return hand.append(random.choice(cards))

def start_game():
    global player_hand, dealer_hand, player_score, dealer_score
    print(art.logo)
    deal_card(player_hand)
    deal_card(player_hand)
    dealer_hand.append('*')
    deal_card(dealer_hand)
    print_hand_info(dealer_hand, 'dealer')
    print_hand_info(player_hand, 'player')


    return

def play_loop(player):
    global player_hand, dealer_hand, player_score, dealer_score
    twist = 'y'
    while twist == 'y':
        my_hand = check_hand(player_hand)

        if my_hand['isBust']:
            print(f'You lose')

        if my_hand['isBlackjack']:
            print(f'You win')

        twist = input("twist? y/n \n").lower()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()
    play_loop('player')