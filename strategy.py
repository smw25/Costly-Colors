import random
import hand as h
#Computer Logic
#Analyze Hand FOR PEGGING (trump card DOESN'T MATTER)
   #[# of Suit, xxx, xxx]
#Sequence (Prials)
def sequence(hand:list):
    hand = hand.copy()
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
        elif card[0:2] == '10':
            hand[inx] = 10
        else:
            hand[inx] = int(card[0])
    ordered = sorted(hand)
    #check to see if these cards are in a sequence
    l_ord = len(ordered)
    value = False 
    #for i in range(l_ord):
    for i in range(l_ord-1, 0, -1):
        if l_ord <= 2:  #if there is only 1 card there cannot be a sequence 
            value = False
            break
        #elif ordered[i] == ordered[i]:
        elif ordered[i-1] +1 == ordered[i]:
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
        for card in c_hand:              #in the computer's hand 
            iplay = c_hand.index(card)   #index integer
            #lcard = [card]
            #v, h, o = sequence(lcard)
            vtotal.append(card)            #ordered list of played down cards from above 
            seq, cc_hand, ordd = sequence(vtotal)   #we only care if by adding a card we get a sequence
            go_test = comp_go(c_hand, current, iplay)
            if seq == True and go_test == False:
                atup = (card, len(ord)) #******************
                options.append(atup)
                break
            else:
                vtotal.pop()
        ord.pop()
        
    #Pairs and Prials
    p_hand = c_hand.copy()
    p_hand, val = pairs(p_hand)
    if len(vtotal) >= 3 and vtotal[-3] == vtotal[-2] == vtotal[-1]: #only can be 4 of a kind
        if vtotal[-1] in p_hand:                #JUST the Number or Face
            ipp = p_hand.index(vtotal[-1])
            #play that card that matches (+18)
            too_big = comp_go(p_hand, current, ipp)
            if too_big == True:
                pass
            else:
                atup = (c_hand[ipp], 18)            #*******
                options.append(atup)
        else: 
            pass
    elif len(vtotal) == 2 and vtotal[-2] == vtotal[-1]:  #three of a kind and 2 cards on the board
        if vtotal[-1] in p_hand: 
            ipp = p_hand.index(vtotal[-1])
            #play that card (+9)
            too_big = comp_go(p_hand, current, ipp)
            if too_big == True:
                pass
            else:
                atup = (c_hand[ipp], 9)            #*******
                options.append(atup)
        else:
            pass
    elif len(vtotal) > 0 and vtotal[-1] in p_hand: 
        ipp = p_hand.index(vtotal[-1])
        #play that card (+2)
        too_big = comp_go(p_hand, current, ipp)
        if too_big == True:
                pass
        else:
            atup = (c_hand[ipp], 2)              #*******
            options.append(atup)

    #Addition
    a_hand = c_hand.copy()
    a_hand = addition(a_hand)
    go_out = []
    over = []   #current = sum of total
    #if current + any number in hand = 15, 25, or 31
    for card in a_hand: #hand is now composed of numerical value of cards
        aind = a_hand.index(card)
        if current + card == 15 or current + card == 25 or current + card == 31:
            addval = len(totalnum) + 1     #how many cards have been played = points for the addition
            atup = (c_hand[aind], addval)
            options.append(atup)
            break
        elif current + card > 31:
            go_out.append(1)
            ii = a_hand.index(card)
            over.append(ii)
            if sum(go_out) == len(a_hand):
                return None
        #elif current + card < 31:
            #playable = True 
        #elif current + card > 31:
            #c_hand.pop()
        else:
            pass
    #if sum(go_out)
    
    
    #Biggest Value 
    if len(options) > 1:
        points = options[0][1]  #options = ((card name, value), (card name, value))
        play_card = options[0][0]
        for x in range(len(options)):
            if options[x][1] > points:
                points = options[x][1]
                play_card = options[x][0]
            else:
                pass
    elif len(options) == 1:
        play_card = options[0][0]
    elif len(options) == 0 and len(c_hand) == 0: #No cards available 
        return None 
    elif len(options) == 0:
        if len(over) != 0:
            for index in over:
                c_hand.pop(index)
        lp = random.choices(c_hand)
        play_card = lp[0]
    return play_card

def mog_choice(hand:list, topcard, a_total):          #What should the number be to mog  
    c_tot = 0 
    testers = []   
    cc_hand = hand.copy()  
    #test the computer's dealt hand with the top card included
    cc_hand.append(topcard)  
    total = h.analyze_3(c_tot, cc_hand)
    cc_hand.pop()   #take out top card
    if total > 4: 
        cmog = 'N'
    elif a_total >= 58:
        cmog = 'Y'
        trader = random.choice(cc_hand)
        tgc = 0     #"too good counter"
        for card in cc_hand:
            if '5' in card or '2' in card or 'Jack' in card:
                tgc +=1 
            else:
                pass 
        if tgc < 3:
            if '5' in trader or '2' in trader or 'Jack' in trader:
                while '5' in trader or '2' in trader or 'Jack' in trader:
                   trader = random.choice(cc_hand)
        elif tgc == 3:
            trader = random.choice(cc_hand)

    elif total == 4:
        t_hand = cc_hand.copy()
        for card in cc_hand:    #cc_hand = [1st card, 2nd card, 3rd card]
            id = t_hand.index(card) 
            c_tot = 0
            #take out the current card of the hand
            t_hand.pop(id)
            #put in the dummy card so your hand is now 4 cards long     [2nd card, 3rd card, dummy]
            t_hand.append('0 of Blank')
            #put in the trump card      [2nd card, 3rd card, dummy, trump,] 
            t_hand.append(topcard)
            t_tot = h.analyze_3(c_tot, t_hand)
            if t_tot == 4:
                cmog = 'Y'
                #if card == '0 of Blank':
                #    candidate = (, t_tot)
                candidate = (cc_hand.index(card), t_tot)
                testers.append(candidate)
            elif t_tot < 4:
                cmog = 'N'
            elif t_tot > 4:
                cmog = 'Y'
                #if card == '0 of Blank':
                #    candidate = (, t_tot)
                candidate = (cc_hand.index(card), t_tot)
                testers.append(candidate)
            t_hand.pop()    #[2nd card, 3rd card, trump, xxdummyxx]
            t_hand.pop()    #[2nd card, 3rd card, xxtrumpxx]
            t_hand.append(card) #[2nd card, 3rd card, 1st card]
        if len(testers) > 0:
            cmog = 'Y'
    elif total < 4:
        t_hand = cc_hand.copy()
        for card in cc_hand:
            c_tot = 0
            id = t_hand.index(card)
            card = t_hand.pop(id)
            t_hand.append('0 of Blank')
            t_hand.append(topcard)
            t_tot = h.analyze_3(c_tot, t_hand)
            if t_tot > total:
                cmog = 'Y'
                #if card == '0 of Blank':
                #    candidate = (cc_hand.index, t_tot)
                candidate = (cc_hand.index(card), t_tot)
                testers.append(candidate)
            elif t_tot < total:
                cmog = 'N'
            elif t_tot == total:
                cmog = 'Y'
                #if card == '0 of Blank':
                #    candidate = (, t_tot)
                candidate = (cc_hand.index(card), t_tot)
                testers.append(candidate)
            t_hand.pop()    #get out trump card
            t_hand.pop()    #get rid of 0 of blank card
            t_hand.append(card) #put back the normal card 
        if len(testers) > 0:
            cmog = 'Y'
    #If cmog = "N" then there will be no candidate cards to test
    if len(testers) == 0:
        return cmog, None
    else:
        v_trader = testers[0][1]
        trader = cc_hand[testers[0][0]]      #[(#, # total value)]  By getting rid of the card at the index (first value) your total hand score equals the second value 
    for i in range(len(testers) -1):
            if testers[i+1][1] > v_trader:      #if the next card in testers provides a higher score
                trader = cc_hand[testers[i+1][0]]   #make the next card the trader card
                v_trader = testers[i+1][1]      #update the higher value when losing the trader card
            elif testers[i+1][1] == v_trader:
                iiit =random.choice(range(i, i+2))
                if '5' not in cc_hand[i+1][1]:
                   trader = cc_hand[i+1][1]
                   v_trader = testers[i+1][1]
                trader = cc_hand[testers[iiit][0]]
            else:
                pass
    return cmog, trader          #should return yes or no AND the string card e.g. '6 of Hearts'