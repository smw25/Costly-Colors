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
        if i == l_ord - 1:  #if there is only 1 card there cannot be a sequence 
            value = False
            break
        elif ordered[i+1] - 1 == ordered[i]:
            value = True
        else: 
           value = False 
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
        #OLD Method
        ind = hand.index(card)
        #hand[ind] = card[0:4]

        parts = card.split(' ')
        hand[ind] = parts[0]
    #ONLY 3 CARDS / IN HAND
    #If the first card equals the second or third we have a pair 
    #if hand[0] == hand[1] or hand[0] == hand[2]:
    #    return hand, True
    #elif hand[1] == hand[2]:
    #    return hand, True
    #else:
    #    return hand, False 
    return hand, None

#Addition to 15, 25, or 31  
def addition(hand:list):
    #hand = hand[1:]
    #turn all cards in hand into their numerical values 
    for card in hand:    
        i = hand.index(card)            
        if card[0:4] == 'Jack' or card[0:4] == "King" or card[0:4] == "Quee":
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

def comp_go(c_hand:list, totalsum, indx):
    go_hand = c_hand.copy()
    go_hand = addition(go_hand)
    if go_hand[indx] + totalsum > 31:
        go = True
    else:
        go = False
    return go

def next_card(totalnum, vtotal, c_hand):  
    #Args:  vtotal = "hand" being played between players 
    #       totalnum = hand as just numbers (no face cards just 10s)
    #       c_hand = the hand dealt to the computer 
    #WHICHEVER GIVES MOST POINTS
    current = sum(totalnum)
    total_len = len(vtotal) 
    options = []  #tuples = ('card of suit', ##)
    
    #Sequencing     
    #--> Just establishes if there is a sequence
    if total_len == 2:
        #3run = sequence(vtotal[-2:])
        run, shand, ord = sequence(vtotal[-2:])
    elif total_len == 3:
        #4run = sequence(vtotal[-3:])
        run, shand, ord = sequence(vtotal[-3:])
    elif total_len >= 4:
        #5run or more = sequence(vtotal[-total_length:])
        run, shand, ord = sequence(vtotal[-total_len:])
    else: #if only 1 card
        run = False
    #Checks if a card in the computer's hand can complete a run on the played cards
    if run == True:
        #the cards are now just their numerical values with face cards having 11, 12, 13
        for card in shand:              #in the computer's hand 
            iplay = shand.index(card)   #index integer
            ord.append(card)            #ordered list of played down cards from above 
            seq, cc_hand, ordd = sequence(ord)   #we only care if by adding a card we get a sequence
            go_test = comp_go(c_hand, current, iplay)
            if seq == True and go_test == False:
                atup = (card, len(ord)) #******************
                options.append(atup)
                break
            else:
                pass
                ord.pop()
        ord.pop()
        
    #Pairs and Prials
    p_hand = c_hand.copy()
    p_hand, val = pairs(p_hand)
    if len(vtotal) >= 3 and vtotal[-3] == vtotal[-2] == vtotal[-1]: #only can be 4 of a kind
        if vtotal[-1] in p_hand:                #JUST the Number or 
            ipp = p_hand.index(vtotal[-1])
            #play that card that matches (+18)
            atup = (p_hand[ipp], 18)            #*******
            options.append(atup)
        else: 
            pass
    elif len(vtotal) == 2 and vtotal[-2] == vtotal [-1]:  #three of a kind and 2 cards on the board
        if vtotal[-1] in p_hand: 
            ipp = p_hand.index(vtotal[-1])
            #play that card (+9)
            atup = (p_hand[ipp], 9)            #*******
            options.append(atup)
        else:
            pass
    elif vtotal[-1] in p_hand: 
        ipp = p_hand.index(vtotal[-1])
        #play that card (+2)
        atup = (p_hand[ipp], 2)              #*******
        options.append(atup)

    #Addition
    a_hand = c_hand.copy()
    a_hand = addition(a_hand)
    #if current + any number in hand = 15, 25, or 31
    for card in a_hand: #hand is now composed of numerical value of cards
        aind = a_hand.index(card)
        if current + card == 15 or current + card == 25 or current + card == 31:
            addval = len(totalnum) + 1     #how many cards have been played = points for the addition
            atup = (c_hand[aind], addval)
            options.append(atup)
            break
        else:
            pass
    
    #Biggest Value 
    if len(options) > 1:
        points = options[0][1]
        for x in range(len(options)):
            if options[x][1] > points:
                points = options[x][1]
                play_card = options[x][0]
            else:
                pass
    elif len(options) == 1:
        play_card = options[0][0]
    elif len(options) == 0:
        lp = random.choices(c_hand)
        play_card = lp[0]
    return play_card