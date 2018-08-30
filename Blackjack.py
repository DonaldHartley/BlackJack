class Deck:
    '''
    This is to create a usable deck of cards as tuples with card lables and blackjack 
    point values
    '''
    # A is Ace, J is Jack, Q is Queen, K is King
    # D is Dimonds, C is Clubs, H is Hearts, S is Spades
    # the varible value od an Ace should be evaluated in the win condtion def
    
    def __init__(self):
        self.deck_list=[('A-D',11),('2-D',2),('3-D',3),('4-D',4),\
                        ('5-D',5),('6-D',6),('7-D',7),('8-D',8),\
                        ('9-D',9),('10-D',10),('J-D',10),('Q-D',10),\
                        ('K-D',10),('A-C',11),('2-C',2),('3-C',3),\
                        ('4-C',4),('5-C',5),('6-C',6),('7-C',7),\
                        ('8-C',8),('9-C',9),('10-C',10),('J-C',10),\
                        ('Q-C',10),('K-C',10),('A-H',11),('2-H',2),\
                        ('3-H',3),('4-H',4),('5-H',5),('6-H',6),\
                        ('7-H',7),('8-H',8),('9-H',9),('10-H',10),\
                        ('J-H',10),('Q-H',10),('K-H',10),('A-S',11),\
                        ('2-S',2),('3-S',3),('4-S',4),('5-S',5),\
                        ('6-S',6),('7-S',7),('8-S',8),('9-S',9),\
                        ('10-S',10),('J-S',10),('Q-S',10),('K-S',10)]

    def drawCard(self):
        '''
        This returns and removes a ramdom card from the current deck list
        '''
        from random import randint
        return self.deck_list.pop(randint(0,len(self.deck_list)-1))

    
class Player():
    '''
    This creates a player to play blackjack with records for money, wins, losses
    and the players current hand 
    '''
    def __init__(self, money=100, wins=0, losses=0, current_hand=[]):
        self.money = money
        self.wins = wins
        self.losses = losses
        self.current_hand = current_hand 
        
    def handPrint(self):
        '''
        This prints just the cards and not the point values
        '''
        hand = [card[0] for card in self.current_hand]
        print (hand)
     
    
     # needs def for reseting the hand to an empty list

# test_player.current_hand += tuple([test_deck.drawCard()])
# use this syntax to add the cards as a tuple to current_hand
