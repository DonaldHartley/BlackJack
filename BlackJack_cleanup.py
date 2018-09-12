class Deck:
    """
    This is to create a usable deck of cards as tuples with card labels
    and blackjack point values
    """
    # the variable value of an Ace is evaluated in the win condition
    def __init__(self):
        self.deck_list = [('ACE of DIAMONDS', 11), ('2 of DIAMONDS', 2), ('3 of DIAMONDS', 3),
                          ('4 of DIAMONDS', 4), ('5 of DIAMONDS', 5), ('6 of DIAMONDS', 6),
                          ('7 of DIAMONDS', 7), ('8 of DIAMONDS', 8), ('9 of DIAMONDS', 9),
                          ('10 of DIAMONDS', 10), ('JACK of DIAMONDS', 10),
                          ('QUEEN of DIAMONDS', 10), ('KING of DIAMONDS', 10),
                          ('ACE of CLUBS', 11), ('2 of CLUBS', 2), ('3 of CLUBS', 3),
                          ('4 of CLUBS', 4), ('5 of CLUBS', 5), ('6 of CLUBS', 6),
                          ('7 of CLUBS', 7), ('8 of CLUBS', 8), ('9 of CLUBS', 9),
                          ('10 of CLUBS', 10), ('JACK of CLUBS', 10), ('QUEEN of CLUBS', 10),
                          ('KING of CLUBS', 10),
                          ('ACE of HEARTS', 11), ('2 of HEARTS', 2), ('3 of HEARTS', 3),
                          ('4 of HEARTS', 4), ('5 of HEARTS', 5), ('6 of HEARTS', 6),
                          ('7 of HEARTS', 7), ('8 of HEARTS', 8), ('9 of HEARTS', 9),
                          ('10 of HEARTS', 10), ('JACK of HEARTS', 10), ('QUEEN of HEARTS', 10),
                          ('KING of HEARTS', 10),
                          ('ACE of SPADES', 11), ('2 of SPADES', 2), ('3 of SPADES', 3),
                          ('4 of SPADES', 4), ('5 of SPADES', 5), ('6 of SPADES', 6),
                          ('7 of SPADES', 7), ('8 of SPADES', 8), ('9 of SPADES', 9),
                          ('10 of SPADES', 10), ('JACK of SPADES', 10), ('QUEEN of SPADES', 10),
                          ('KING of SPADES', 10)]

    def draw_card(self):
        """
        This returns and removes a random card from the current deck list
        """
        from random import randint
        return self.deck_list.pop(randint(0, len(self.deck_list) - 1))

    def shuffle_deck(self):
        """
        This resets the deck
        """
        self.deck_list = [('ACE of DIAMONDS', 11), ('2 of DIAMONDS', 2), ('3 of DIAMONDS', 3),
                          ('4 of DIAMONDS', 4), ('5 of DIAMONDS', 5), ('6 of DIAMONDS', 6),
                          ('7 of DIAMONDS', 7), ('8 of DIAMONDS', 8), ('9 of DIAMONDS', 9),
                          ('10 of DIAMONDS', 10), ('JACK of DIAMONDS', 10),
                          ('QUEEN of DIAMONDS', 10), ('KING of DIAMONDS', 10),
                          ('ACE of CLUBS', 11), ('2 of CLUBS', 2), ('3 of CLUBS', 3),
                          ('4 of CLUBS', 4), ('5 of CLUBS', 5), ('6 of CLUBS', 6),
                          ('7 of CLUBS', 7), ('8 of CLUBS', 8), ('9 of CLUBS', 9),
                          ('10 of CLUBS', 10), ('JACK of CLUBS', 10), ('QUEEN of CLUBS', 10),
                          ('KING of CLUBS', 10),
                          ('ACE of HEARTS', 11), ('2 of HEARTS', 2), ('3 of HEARTS', 3),
                          ('4 of HEARTS', 4), ('5 of HEARTS', 5), ('6 of HEARTS', 6),
                          ('7 of HEARTS', 7), ('8 of HEARTS', 8), ('9 of HEARTS', 9),
                          ('10 of HEARTS', 10), ('JACK of HEARTS', 10), ('QUEEN of HEARTS', 10),
                          ('KING of HEARTS', 10),
                          ('ACE of SPADES', 11), ('2 of SPADES', 2), ('3 of SPADES', 3),
                          ('4 of SPADES', 4), ('5 of SPADES', 5), ('6 of SPADES', 6),
                          ('7 of SPADES', 7), ('8 of SPADES', 8), ('9 of SPADES', 9),
                          ('10 of SPADES', 10), ('JACK of SPADES', 10), ('QUEEN of SPADES', 10),
                          ('KING of SPADES', 10)]


class Player:
    """
    This creates a player/dealer to play blackjack with records for
    money, wins, losses and the players current hand
    """
    def __init__(self, money=100, wins=0, losses=0, bet=0, bet_raise=0):
        self.money = money
        self.wins = wins
        self.losses = losses
        self.current_hand = []
        self.bet = bet
        self.bet_raise = bet_raise

    def hand_print(self):
        """
        This prints just the cards and not the point values
        """
        hand = [card[0] for card in self.current_hand]
        print(hand)

    def new_hand(self):
        """
        clears the player hand for a new game
        """
        self.current_hand = []

    def check_points(self):
        """
        This checks the points for the ACE adjustment and returns the sum of
        the points of the cards in the current_hand
        """
        global points_eval
        points_hand = [card[1] for card in self.current_hand]
        points_eval = True
        # the returns are adjusted points values
        while points_eval:
            if sum(points_hand) <= 21:
                points_eval = False
                return sum(points_hand)
            elif sum(points_hand) > 21:
                if 11 in points_hand:
                    points_hand[points_hand.index(11)] = 1
                    continue
                else:
                    points_eval = False
                    return sum(points_hand)


def player_input():
    """
    This takes a player input and returns the first letter
    in lowercase to evaluate it against the available options
    h for hit, s for stand, b for bet, q for quit, r for raise
    """
    player_says = input()
    return player_says[0].lower()
    # returns first letter lowercase


player_one = Player()
dealer = Player()
the_shoe = Deck()
player_hand_results = 0
dealer_hand_results = 0
response = ''
play = False
this_hand = False
ask = False
dealer_check = False
raise_bet = False
points_eval = False


def game_board():
    """
    This prints the game board for each play made
    """
    print(f'|Player |Money: {player_one.money} |Bet amount: {player_one.bet} |Wins: {player_one.wins} \
    |Losses: {player_one.losses} |\n')
    print(f'|Dealers hand: ')
    dealer.hand_print()
    print('\n')
    print('|Players hand: ')
    player_one.hand_print()
    print('\n-----')


def start_hand():
    """
    This prints the start a new hand board and player prompt
    """
    global response
    global player_one
    global dealer
    global the_shoe
    global player_hand_results
    global dealer_hand_results
    global play
    global this_hand
    global ask
    global dealer_check
    global raise_bet
    game_board()
    print('Would you like to BET on a new hand or QUIT?\n')
    response = ''
    ask = True
    while ask:
        response = player_input()  # returns first letter lowercase
        if response not in 'bq':
            print('Please make a valid selection\n')
            print('Would you like to BET on a new hand or QUIT?\n')
            continue
        elif response == 'b':
            betting = True
            while betting:
                print('How much would you like to bet?\n')
                player_one.bet = int(input())
                if player_one.bet > player_one.money:
                    print(f'\nYou only have {player_one.money} available, {player_one.bet} \
                           is too much.\nPlease choose a different amount\n')
                    continue
                elif player_one.bet <= 0:
                    print(f'\n{player_one.bet} is not a valid amount please try \
                           again.\n')
                    continue
                elif player_one.bet <= player_one.money:
                    print('Ok, lets begin!\n\n')
                    player_one.money -= player_one.bet
                    dealer.current_hand += tuple([the_shoe.draw_card()])
                    player_one.current_hand += tuple([the_shoe.draw_card()])
                    player_one.current_hand += tuple([the_shoe.draw_card()])
                    game_board()
                    play_check()
                    betting = False
                    ask = False
                else:
                    print(f'\n{player_one.bet} is not a valid number please try again.\n')
                    continue
        elif response == 'q':
            print('Thank you for playing!')
            play = False
            this_hand = False
            ask = False


def hit_raise_stand():
    """
    This is so the player can choose their next action
    """
    global response
    global player_one
    global dealer
    global the_shoe
    global player_hand_results
    global dealer_hand_results
    global play
    global this_hand
    global ask
    global dealer_check
    global raise_bet
    response = ''
    ask = True
    while ask:
        print('\nWould you like to HIT, RAISE or STAND?\n')
        response = player_input()  # returns first letter lowercase
        if response not in 'rsh':
            print('\nThat is not a valid response. ')
            continue
        elif response == 'r':
            raise_bet = True
            while raise_bet:
                print('\nOk Raise, how much would you like to raise?\n')
                player_one.bet_raise = int(input())
                if player_one.bet_raise > player_one.money:
                    print(f'\nYou only have {player_one.money} available, \
                           {player_one.bet_raise} is too much.\nPlease choose a \
                           different amount\n')
                    continue
                elif player_one.bet_raise <= 0:
                    print(f'\n{player_one.bet_raise} is not a valid amount please try \
                           again.\n')
                    continue
                elif player_one.bet_raise <= player_one.money:
                    print('Ok\n\n')
                    player_one.money -= player_one.bet_raise
                    player_one.bet += player_one.bet_raise
                    player_one.bet_raise = 0
                    player_one.current_hand += tuple([the_shoe.draw_card()])
                    play_check()
                else:
                    print(f'\n{player_one.bet_raise} is not a valid number \
                           please try again.\n')
                    continue
        elif response == 's':
            print('Ok Stand\n\n')
            ask = False
        elif response == 'h':
            print('Ok Hit\n\n')
            player_one.current_hand += tuple([the_shoe.draw_card()])
            play_check()


def play_check():
    """
    this checks if the player wins or busts
    """
    global response
    global player_one
    global dealer
    global the_shoe
    global player_hand_results
    global dealer_hand_results
    global play
    global this_hand
    global ask
    global dealer_check
    global raise_bet
    game_board()
    player_hand_results = player_one.check_points()
    # returns are adjusted points values
    if player_hand_results == 21:
        print('21 you Win!')
        player_one.money += (player_one.bet*2)
        player_one.bet = 0
        player_one.wins += 1
        player_one.new_hand()
        dealer.new_hand()
        the_shoe.shuffle_deck()
        this_hand = False
        raise_bet = False
        ask = False
        response = ''
    elif player_hand_results > 21:
        player_one.bet = 0
        player_one.losses += 1
        player_one.new_hand()
        dealer.new_hand()
        the_shoe.shuffle_deck()
        this_hand = False
        raise_bet = False
        ask = False
        response = ''
        print('You Bust, House Wins')


def dealer_acts():
    """
    this runs the dealers actions
    """
    global response
    global player_one
    global dealer
    global the_shoe
    global player_hand_results
    global dealer_hand_results
    global play
    global this_hand
    global ask
    global dealer_check
    global raise_bet
    dealer.current_hand += tuple([the_shoe.draw_card()])
    dealer_hand_results = dealer.check_points()
    player_hand_results = player_one.check_points()
    # returns are adjusted points values
    dealer_check = True
    while dealer_check:
        game_board()
        if dealer_hand_results < 17:
            dealer.current_hand += tuple([the_shoe.draw_card()])
            dealer_hand_results = dealer.check_points()
            continue
        elif dealer_hand_results == 21:
            print('House Wins')
            player_one.bet = 0
            player_one.losses += 1
            player_one.new_hand()
            dealer.new_hand()
            the_shoe.shuffle_deck()
            this_hand = False
            dealer_check = False
        elif 17 <= dealer_hand_results < 21:
            point_check = player_hand_results-dealer_hand_results
            if point_check < 0:
                print('House Wins')
                player_one.bet = 0
                player_one.losses += 1
                player_one.new_hand()
                dealer.new_hand()
                the_shoe.shuffle_deck()
                this_hand = False
                dealer_check = False
            elif point_check > 0:
                print('Player Wins!')
                player_one.money += (player_one.bet*2)
                player_one.bet = 0
                player_one.wins += 1
                player_one.new_hand()
                dealer.new_hand()
                the_shoe.shuffle_deck()
                this_hand = False
                dealer_check = False
            elif point_check == 0:
                print('Push')
                player_one.money += player_one.bet
                player_one.bet = 0
                player_one.new_hand()
                dealer.new_hand()
                the_shoe.shuffle_deck()
                this_hand = False
                dealer_check = False
        elif dealer_hand_results > 21:
            print('House busts, you Win!')
            player_one.money += (player_one.bet*2)
            player_one.bet = 0
            player_one.wins += 1
            player_one.new_hand()
            dealer.new_hand()
            the_shoe.shuffle_deck()
            this_hand = False
            dealer_check = False
