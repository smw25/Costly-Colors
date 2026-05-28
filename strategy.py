import random
 
#Computer Logic

#Analyze Hand FOR PEGGING (trump card DOESN'T MATTER)
   #[# of Suit, xxx, xxx]

#Sequence (Prials)
def sequence(hand:list):
    #hand = hand[1:]
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
            hand[inx] = int(card[0])
    ordered = sorted(hand)
    #check to see if these cards are in a sequence
    #l_len = len(ordered)
    #for i in range(l_len)
    #if ordered[i] == ordered[i+1]
    #   continue / True
    #else 
    #   False and ?break?      
    run_1 = ordered[1] - 1
    run_2 = ordered[2] - 1
    if (ordered[0] == run_1) and (ordered[1] == run_2):
        mid = ordered[1]
        return True, hand, mid
    else:
        return False, hand, None 

#Pairs 
def pairs(hand:list):
    #hand = hand[1:]   if the length of the hand is at least 3 
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
    #hand = hand[1:]
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
#In theory the sequence, pair, and addition functions can be used for the running total on the board
#in this way the computer would be able to analyze this and choose cards based upon what would be more advantageous pointwise
#How to implement this on GOs?????

#WHICHEVER GIVES MOST POINTS
#current = sum(ntotal)
#surrent = total 
#3run = sequence(total[-2:])
#4run = sequence(total[-3:])
#5run = sequence(total[-4:])

#if current + any number in hand = 15, 25, or 31
    #play that card (add it to total and do the analyze thing)

#Pairs and Prials
#if len(total) >= 3 and total[-3] == total[-2] == total[-1] and any card in hand == total[-1]
    #play that card that matches (+18)
#if total[-2] == total [-1] and any card in hand == total[-1]
#   play that card (+9)
# if total[-1] == any card in hand 
#   play that card (+2)

