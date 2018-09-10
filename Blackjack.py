class Deck:
    '''
    This is to create a usable deck of cards as tuples with card lables
    and blackjack point values
    '''
    # the varible value of an Ace should be evaluated in the win condtion def
    def __init__(self):
        self.deck_list=[('ACE of DIMONDS',11),('2 of DIMONDS ',2),('3 of DIMONDS ',3),\
                        ('4 of DIMONDS ',4),('5 of DIMONDS ',5),('6 of DIMONDS ',6),\
                        ('7 of DIMONDS ',7),('8 of DIMONDS ',8),('9 of DIMONDS ',9),\
                        ('10 of DIMONDS ',10),('JACK of DIMONDS ',10),\
                        ('QUEEN of DIMONDS ',10),('KING of DIMONDS ',10),\
                        ('ACE of CLUBS',11),('2 of CLUBS',2),('3 of CLUBS',3),\
                        ('4 of CLUBS',4),('5 of CLUBS',5),('6 of CLUBS',6),\
                        ('7 of CLUBS',7),('8 of CLUBS',8),('9 of CLUBS',9),\
                        ('10 of CLUBS',10),('JACK of CLUBS',10),('QUEEN of CLUBS',10),\
                        ('KING of CLUBS',10),\
                        ('ACE of HEARTS',11),('2 of HEARTS',2),('3 of HEARTS',3),\
                        ('4 of HEARTS',4),('5 of HEARTS',5),('6 of HEARTS',6),\
                        ('7 of HEARTS',7),('8 of HEARTS',8),('9 of HEARTS',9),\
                        ('10 of HEARTS',10),('JACK of HEARTS',10),('QUEEN of HEARTS',10),\
                        ('KING of HEARTS',10),\
                        ('ACE of SPADES',11),('2 of SPADES',2),('3 of SPADES',3),\
                        ('4 of SPADES',4),('5 of SPADES',5),('6 of SPADES',6),\
                        ('7 of SPADES',7),('8 of SPADES',8),('9 of SPADES',9),\
                        ('10 of SPADES',10),('JACK of SPADES',10),('QUEEN of SPADES',10),\
                        ('KING of SPADES',10)]

    def drawCard(self):
        '''
        This returns and removes a ramdom card from the current deck list
        '''
        from random import randint
        return self.deck_list.pop(randint(0,len(self.deck_list)-1))

class Player():
    '''
    This creates a player/dealer to play blackjack with records for 
    money, wins, losses and the players current hand 
    '''

    def __init__(self, money=100, wins=0, losses=0, bet=0, current_hand=[]):
        self.money = money
        self.wins = wins
        self.losses = losses
        self.current_hand = current_hand
        self.bet = bet

    def handPrint(self):
        '''
        This prints just the cards and not the point values
        '''
        hand = [card[0] for card in self.current_hand]
        print (hand)

    def newHand(self):
        '''
        clears the player hand for a new game
        '''
        self.current_hand=[]

    def checkPoints(self):
        '''
        This checks the points for the ACE adjustment and returns the sum of
        the points of the cards in the current_hand
        '''
        points_hand = [card[1] for card in self.current_hand]
        points_eval = True
        # the returns are adjusted points values
        while points_eval:
            if sum(points_hand)<=21:
                points_eval = False
                return sum(points_hand)
            elif sum(points_hand)>21:
                if 11 in points_hand:
                    points_hand[points_hand.index(11)]=1
                    continue
                else:
                    points_eval = False
                    return sum(points_hand)

def play_blackjack():
    '''
    This is the function to run the game blackjack
    '''
    play = True
    player_one = Player()
    dealer = Player()
    the_shoe = Deck()
    player_hand_results = 0
    dealer_hand_results = 0
    bet = False
    bet_raise = False
    this_hand = True
    
    
    def game_board():
        '''
        This prints the game board for each play made
        '''
        print(f'|Player |Money: {player_one.money} |Bet ammount: {player.bet} \
              |Wins: {player_one.wins} |Losses: {player_one.losses} |\n\n')
        print(f'|Dealers hand: ')
        dealer.handPrint() 
        print('|\n\n')
        print('|Players hand: ')
        player_one.handPrint()
        print('|\n\n')
    
    def start_hand():
        '''
        This prints the start a new hand board and player prompt
        '''
        print(f'|Player |Money: {player_one.money} |Bet ammount: {player.bet} \
              |Wins: {player_one.wins} |Losses: {player_one.losses} |\n\n')
        print('Would you like to BET on a new hand or QUIT?\n')
        ask=True
        while ask:
            player_choise=player_imput()
            if player_choise!=('b' or 'q'):
                print('Please make a vaild selection\n')
                print('Would you like to BET on a new hand or QUIT?\n')
                continue
            elif player_choise == 'b':
                bet=True
                while bet:
                    print('How nuch would you like to bet?\n')
                    player.bet = input()
                    if player.bet != int:
                        print (f'\n{player_bet} is not a valid number please try again.\n')
                        continue
                    elif player.bet > player.money:
                        print (f'\nYou only have {player.money} available, {player_bet} \
                               is too much.\nPlease choose a different ammount\n')
                        continue
                    elif player.bet<=0:
                        print (f'\n{player_bet} is not a valid ammount please try \
                               again.\n')
                        continue
                    elif player.bet<player.money:
                        print('Ok, lets begin!\n\n')
                        player.money -= player.bet
                        dealer.current_hand += tuple([the_shoe.drawCard()])
                        dealer.current_hand += tuple([the_shoe.drawCard()])
                        player.current_hand += tuple([the_shoe.drawCard()])
                        player.current_hand += tuple([the_shoe.drawCard()])
                        bet=False
                        ask=False
            elif player_choise == 'q':
                print('Thank you for playing!')
                play=False
                ask=False
    
    def player_input():
        '''
        This takes a player input and returns the first letter
        in lowercase to evaluate it against the available options
        h for hit, s for stand, b for bet, q for quit, r for raise
        '''
        player_says = input()
        return player_says[0].lower()
    
        
    
    def bet_raise():
        bet_raise=True
        while bet_raise:
    
    # The game logic starts here
    print ('Welcome to the table. Lets play BlackJack!\n')
    while play:
        while this_hand:
            start_hand()
            game_board()
            player_hand_results = player.checkPoints()
            dealer_hand_results = dealer.checkPoints()
            # returns are adjusted points values
            if player_hand_results==dealer_hand_results==21:
                print ('Draw')
        
            
        

# betting/hand_loss test needs check condition for if player.money=0  
# player imput needs modified for error correction in input def
# needs a raise/hit/stay rules
# needs betting rules
# needs player recordkeeping rules
# needs dealer ai hit/stay rules
# needs win check condition compairing player and dealer, [points, end hand, win hand]

# test_player.current_hand += tuple([test_deck.drawCard()])
# use this syntax to add the cards as a tuple to current_hand
