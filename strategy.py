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
    l_ord = len(ordered)
    for i in range(l_ord):
        if i == l_ord - 1:
            break
        elif ordered[i+1] - 1 == ordered[i]:
            value = True
        else: 
           value = False 
           mid = None
           break     
    return value, hand, ordered  #hand now has numbers for jack queen king
    #OLD SEQUENCE CHECK#
    # if len(ordered) == 3
    #run_1 = ordered[1] - 1
    #run_2 = ordered[2] - 1
    #if (ordered[0] == run_1) and (ordered[1] == run_2):
    #    mid = ordered[1]
    #    return True, hand, mid
    #else:
    #    return False, hand, None 

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
def addition(hand:list):
    #hand = hand[1:]
    #turn all cards in hand into their numerical values 
    for card in hand:    
        i = hand.index(card)            
        if card[0:4] == 'Jack' or "King" or "Quee":
            hand[i] = int(10) 
        elif card[0:3] == 'Ace':
            hand[i] = int(1)
        elif card[0:2] == '10':
            hand[i] = int(10)
        else: 
            hand[i] = int(card[0])
    return hand

#First Card: Computer is non-dealer (goes first)
def first_card_non(s_hand, svalue, s_ordered):
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
        midi = len(s_ordered)//2
        mid = s_ordered[midi]
        for x in range(len(s_hand)):
            if s_hand[x] == mid:
               weights.append(9)
            else:
               weights.append(1)
    else:
        for x in range(len(s_hand)):
            weights.append(1)
    return weights

def comp_go(c_hand, totalnum, indx):
    c_hand = addition(c_hand)
    if c_hand[indx] + totalnum > 31:
        go = True
    else:
        go = False
    return go

def next_card(totalnum, vtotal, c_hand):  
    #Args:  vtotal = "hand" being played between players 
    #       totalnum = hand as just numbers (no face cards just 10s)
    #       c_hand = the hand dealt to the computer 
#In theory the sequence, pair, and addition functions can be used for the running total on the board
#in this way the computer would be able to analyze this and choose cards based upon what would be more advantageous pointwise
#How to implement this on GOs?????

    #WHICHEVER GIVES MOST POINTS
    current = sum(totalnum)
    total_len = len(vtotal) 
    
    #Sequencing     --> Just establishes if there is a sequence
    if total_len == 2:
        #3run = sequence(vtotal[-2:])
        run, c_hand, ord = sequence(vtotal[-2:])
    elif total_len == 3:
        #4run = sequence(vtotal[-3:])
        run, c_hand, ord = sequence(vtotal[-3:])
    elif total_len >= 4:
        #5run = sequence(vtotal[-4:])
        run, c_hand, ord = sequence(vtotal[-4:])
    else: #if only 1 card
        pass
    
    if run == True:
        for card in c_hand: 
            ord.append(card)
            seq, c_hand, ord = sequence(ord)
            if seq == True:
                play = c_hand.index(card)
     
                #Play that card 
    #Pairs and Prials
    #if len(vtotal) >= 3 and vtotal[-3] == vtotal[-2] == vtotal[-1] 
    #   and any card in hand == vtotal[-1]
        #play that card that matches (+18)
    #if vtotal[-2] == vtotal [-1] 
    # and any card in hand == vtotal[-1]
    #   play that card (+9)
    # if vtotal[-1] == any card in hand 
    #   play that card (+2)

#Addition
    #if current + any number in hand = 15, 25, or 31
    c_hand = addition(c_hand)
        #play that card (add it to total and do the analyze thing)