import random
from costly import b 
#Computer Logic

#Analyze Hand FOR PEGGING (trump card DOESN'T MATTER)
hand = b[1:4]   #[# of Suit, xxx, xxx]

#Sequence (Prials)
def sequence(hand:list):
    hand = hand[1:]
    #turn all cards in hand into their respective numerical order
    for card in hand:  
        inx = hand.index(card)              
        if card[0:4] == 'Jack':
            hand[inx] = 11
        elif card[0:4] == 'Quee':
            hand[inx] = 12
        elif card[0:4] == 'King':
            hand[inx] = 13
        elif card[0:3] == 'Ace':
            hand[inx] = 1
        else:
            hand[inx] == int(card[0])
    ordered = sorted(hand)
    #check to see if these cards are in a sequence
    run_1 = ordered[1] - 1
    run_2 = ordered[2] - 1
    if (ordered[0] == run_1) and (ordered[1] == run_2):
        mid = ordered[1]
        return True, hand, mid
    else:
        return False, hand, None 

#Pairs 
def pairs(hand:list):
    hand = hand[1:]
    for card in hand:
        ind = hand.index(card)
        hand[ind] = card[0:4]
    #If the first card equals the second or third we have a pair 
    if hand[0] == hand[1] or hand[0] == hand[2]:
        return True
    elif hand[1] == hand[2]:
        return True
    else:
        return False 

#Addition to 15, 25, or 31  
def addition(hand):
    hand = hand[1:]
    #turn all cards in hand into their numerical values 
    for card in hand:                
        if card[0:4] == 'Jack' or "King" or "Quee":
            card = int(10) 
        elif card[0:3] == 'Ace':
            card = int(1)
        elif card[0:2] == '10':
            card = int(10)
        else: 
            card = int(card[0])
    
seq_value, seq_hand, middle = sequence(hand)
pairs(hand)
addition(hand)

#First Card: Computer is non-dealer (goes first)
def first_card_non(s_hand, svalue, midd):
    weights = []
    if 5 in s_hand:
        for x in range(len(s_hand)):
            if s_hand[x] == 5:
               weights.append(1)  
            else: 
                weights.append(9)
    elif 1 in s_hand:
        for x in range(len(s_hand)):
            if s_hand[x] == 1:
               weights.append(2)  
            else: 
                weights.append(8)
    elif svalue == True:
        for x in range(len(s_hand)):
            if s_hand[x] == midd:
               weights.append(9)
            else:
               weights.append(1)
    else:
        for x in range(len(s_hand)):
            weights.append(1)
    return weights

    #def adding_totals(ntotal, total):
