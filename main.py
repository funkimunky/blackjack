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


def get_score(hand):
    score = {'softscore':'','hardscore':''}
    if(11 in hand):
        score['softscore'] = get_soft_score(hand)
        score['hardscore'] = get_hard_score(hand)
    else:
        score['hardscore'] = sum(hand)

    return score


def check_hand(hand):
    params = {'isBust': False, 'isBlackjack': False}
    if check_bust(hand):
        params['isBust'] = True
        return params

    if check_blackjack(hand):
        params['isBlackjack'] = True
        return params

    return params


def check_bust(hand):
    soft_score = 0

    if 11 in hand:
        soft_score = get_soft_score(hand)

    hard_score = get_hard_score(hand)

    if soft_score > 21 or hard_score > 21:
        return True

    return False


def check_blackjack(hand):
    soft_score = 0

    if 11 in hand:
        soft_score = get_soft_score(hand)

    hard_score = get_hard_score(hand)

    if soft_score == 21 or hard_score == 21:
        return True

    return False
    return


def get_hard_score(hand):
    return sum(hand)


def get_soft_score(hand):
    soft_hand = [x if x != 11 else 1 for x in hand]
    return sum(soft_hand)


def clean_hand(hand):
    cleaned_hand = [x for x in hand if x != '*']
    return cleaned_hand


def print_hand_info(hand, name):
    cleaned_hand = clean_hand(hand)
    print(f'{name}\'s hand \n{hand}\nscore:{get_score(cleaned_hand)}')
    return


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