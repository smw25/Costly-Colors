import random
from costly import b
#Computer Logic

#Analyze Hand
hand = b[1:3] 

#Sequence (Prials)
def sequence(hand):
    #turn all cards in hand into their respective numerical order
    for card in hand:                
        if card[0:3] == 'Jack':
            card = 11
        if card[0:3] == 'Quee':
            card = 12
        if card[0:3] == 'King':
            card = 13
        if card[0:2] == 'Ace':
            card = 1
        else:
            card == int(card[0])
    ordered = sorted(hand)
    #check to see if these cards are in a sequence
    run_1 = hand[1] - 1
    run_2 = hand[2] - 1
    if (hand[0] == run_1) and (hand[1] == run_2):
        return True
    else:
        return False 

def pairs(hand):
    for card in hand:
        card = card[0:3]
    if hand[0] == hand[1] or hand[2]:
        return True
    elif hand[1] == hand[2]:
        return True
    else:
        return False 

#Addition to 15, 25, or 31  
def addition(hand):
    #turn all cards in hand into their numerical values 
    for card in hand:                
        if card[0:3] == 'Jack' or "King" or "Quee":
            card = int(10) 
        elif card[0:2] == 'Ace':
            card = int(1)
        elif card[0:1] == '10':
            card = int(10)
        else: 
            card = int(card[0])
    

sequence(hand)
#First Card: We 
#for card in b[1:3]:
