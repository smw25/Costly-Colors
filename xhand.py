import random
import itertools as it
import xcostly as c 
import strategy as s 
import time as t
import random as r 
#hearts and 
#we can either hard wire or make this more general 
def analyze_2(player_tot, p_hand:list, game):
    #colors first 
    red = False
    blk = False
    rc = 0
    bc = 0
    v_hand = []
    c_hand = []
    dp = None
    str_pri = None
    str_pair = None


    for card in p_hand:
        info = card.split()
        v_hand.append(info[0])  #value
        c_hand.append(info[2])  #suit "color"

    for card in c_hand:
        if card == 'Diamonds'  or card == 'Hearts':
            red = True
            rc += 1
        else: #'Clubs' in card or 'Spades' in card: #else 
            blk = True  
            bc += 1
    unique_suits = set(c_hand)
    suit_c = max(unique_suits, key=c_hand.count)   # the suit with the highest count
    count = c_hand.count(suit_c)
    #suit_c = c_hand[0]
    if red == True and blk == True: 
        pass #keep going
    elif (red == True and blk == False) or (red == False and blk == True):  #All red/black cards
        if all(suit_c == card for card in c_hand) == True: #All same suit 
            player_tot += 6
            #print('Costly Colours! (4 ' + suit_c + '): +6 \n' )
            game.handages.append('Costly Colours! (4 ' + suit_c + '): +6')
        elif sum(suit_c == card for card in c_hand) == 3:   #3 cards same suit 
            player_tot += 5
            #print('4 in Colour, 3 in Suit (' + suit_c + '): +5 \n')
            game.handages.append('4 in Colour, 3 in Suit (' + suit_c + '): +5')
        elif sum(suit_c == card for card in c_hand) == 2:    #2 cards in same suit 
            player_tot += 4
            #print('4 in Colour, 2 in Suit (' + suit_c + '): +4 \n')
            game.handages.append('4 in Colour, 2 in Suit (' + suit_c + '): +4')
    elif c_hand.count(suit_c) == 3: #3 cards same suit & NOT ALL same color 
        player_tot += 3
        #print('3 in Suit (' + suit_c + '): +3') 
        game.handages.append('3 in Suit (' + suit_c + '): +3')
    if (red == True and bc == 1):     #3 in Color
        player_tot += 2 
        #print('3 in Color (Red): +2 \n')
        game.handages.append('3 in Color (Red): +2')
    elif (blk == True and rc == 1):   
        player_tot += 2
        #print('3 in Color (Black): +2 \n')  
        game.handages.append('3 in Color (Black): +2')        
        
    #nobs and duces second
    for i in range(len(v_hand[0:3])):
        if v_hand[i] == 'Jack' and c_hand[i] == c_hand[-1]: #suit of the jack matches the suit of turned up card
            player_tot += 4
            #print('His Nobs: +4 \n')
            game.handages.append('His Nobs: +4')
        elif v_hand[i] == '2' and c_hand[i] == c_hand[-1]:  #suit of the deuce matches the suit of turned up card
            player_tot += 4
            #print('Right Deuce: +4 \n')
            game.handages.append('Right Deuce: +4')
        elif v_hand[i] == 'Jack' or v_hand[i] == '2':
            player_tot += 2
            #print('Jack or Duece in Hand: +2 \n')
            game.handages.append('Jack or Duece in Hand: +2')
        else:
            pass

    #pairs third
    #make cards just their value: 'King' or '5'
    pp_hand = p_hand.copy()
    for card in pp_hand:
        cind = pp_hand.index(card)
        vitals = card.split(' ')
        pp_hand[cind] = vitals[0]

    if pp_hand[0] == pp_hand[1] == pp_hand[2] == pp_hand[3]:
        player_total += 18
        dp = str(pp_hand[0])
        #print('Double Prial (4-of-a-kind) of ' + dp + 's: +18 \n')
        game.handages.append('Double Prial (4-of-a-kind) of ' + dp + 's: +18')

    for prial in it.combinations(pp_hand, 3):
        if prial[0] == prial[1] == prial[2]:
            str_pri = str(prial[0])
            if str_pri == dp:
                break
            player_tot += 9
            #print('Prial of ' + str_pri + 's: +9 \n')
            game.handages.append('Prial of ' + str_pri + 's: +9')

    for pair in it.combinations(pp_hand, 2):
        if pair[0] == pair [1]:
            str_pair = str(pair[0])
            if str_pair == str_pri:     #should stop a lesser pair from being counted from the same trips
                break
            player_tot += 2
            #print('Pair of ' + str_pair + 's: +2 \n')  
            game.handages.append('Pair of ' + str_pair + 's: +2')      

    #addition fifth
    #find indexes of face cards
    add_hand = p_hand.copy()
    tenxs = []
    for card in add_hand:
        if 'Jack' in card[0:4] or 'Quee' in card[0:4] or 'King' in card[0:4] or '10' in card[0:2]:
            findx = add_hand.index(card)
            tenxs.append(findx)
    counter = 0
    #make cards in their numerical values for counting 
    add_hand = s.addition(add_hand)
    #If ALL 4 cards add a Number
    if sum(add_hand) == 15 or sum(add_hand) == 25 or sum(add_hand) == 31:
        player_tot += 4
        #print('All 4 cards = ' + str(sum(add_hand)) + ': +4 \n')
        game.handages.append('All 4 cards = ' + str(sum(add_hand)) + ': +4')
    
    #The summation of three cards can ONLY equal 15 or 25 
    for triple in it.combinations(add_hand, 3):
        if sum(triple) == 15 or sum(triple) == 25:
            if 10 in triple and len(tenxs) > 1:
                kick = p_hand[tenxs[counter]]
                #print(triple, end='')
                #print(' -------> ' + kick)
                game.handages.append(str(triple) + ' -------> ' + kick)
                #game.handages.append()
                counter += 1
            elif 10 in triple and len(tenxs) == 1:
                kick = p_hand[tenxs[0]]
                #print(triple, end='')
                #print(' -------> ' + kick)
                game.handages.append(str(triple) + ' -------> ' + kick)
                #game.handages.append(' -------> ' + kick)
            else: 
                #print(triple)
                game.handages.append(triple)
            player_tot += 3
            #print('Sum to ' + str(sum(triple)) + ': +3 \n')
            game.handages.append('Sum to ' + str(sum(triple)) + ': +3')
    counter = 0

    #The summation of any two cards can only equal 15
    for combo in it.combinations(add_hand, 2):
        if sum(combo) == 15:
            if 10 in combo and len(tenxs) == 1:  #works with having one 10 card and multiple othe fifteens
                kick = p_hand[tenxs[0]]   #counter == 0 
                #print(combo, end='')
                #print(' -------> ' + kick)
                game.handages.append(str(combo) + ' -------> ' + kick)
                #game.handages.append()
            elif 10 in combo and len(tenxs) > 1: #works with multiple 10s 
                kick = p_hand[tenxs[counter]]
                #print(combo, end='')
                #print(' -------> ' + kick)
                game.handages.append(str(combo) + ' -------> ' + kick)
                #game.handages.append(' -------> ' + kick)
                counter += 1
            else: 
                #print(combo)
                game.handages.append(combo)
            player_tot += 2
            #print('Sum to 15: +2 \n')
            game.handages.append('Sum to 15: +2')
    counter = 0

    return player_tot

def round_totals(user_total, comp_total, pa, pb, game): 
    #total for the round, computer total for round, pegging totals, game class
    #print('*#*#*Round Toals*#*#*')
    game.handages.append('#*#*#*#*#*#* Round Toals *#*#*#**#*#*')
    
    ut = str(user_total)  #useer
    ct = str(comp_total)
    pas = str(pa)         #user's pegging
    pbs = str(pb)         #comp's pegging
    #Computer Hand
    #print('---Mr. Crib---')
    game.handages.append('---Mr. Crib---')
    #print("Pegging = " + pbs)
    game.handages.append("Pegging = " + pbs)
    #print("Hand = " + str(comp_total - pb))
    game.handages.append("Hand = " + str(comp_total - pb))
    #print("Mr. Crib's Total = " + ct + "\n")
    game.handages.append("Mr. Crib's Total = " + ct)
    game.handages.append(" ")

    #user
    #print('---You---') 
    game.handages.append('---You---')
    #print('Pegging = ' + pas)
    game.handages.append('Pegging = ' + pas)
    #print("Hand = " + str(user_total - pa))
    game.handages.append("Hand = " + str(user_total - pa))
    #print('Your Total = ' + ut)
    game.handages.append('Your Total = ' + ut)

def grand_totals(game):
    #print('\n*#*#*Grand Totals*#*#*')
    game.handages.append(' ')
    game.handages.append('*#*#*Grand Totals*#*#*')
    game.player_score += game.player_rsco
    game.computer_score += game.comp_rsco
    #print('Mr. Crib = ' + str(game.computer_score))
    game.handages.append('Mr. Crib = ' + str(game.computer_score))
    #print("Your's = " + str(game.player_rsco))
    game.handages.append("Your's = " + str(game.player_score))
    card_deck = c.return_cards(game.player_played, game.computer_played, game.top, game.deck)
    game.deck = card_deck

    if game.player_hand[0] == '*D*': #if user was dealer
        game.player_hand[0] = '#'    #user is now pone
    else:
        game.player_hand[0] = '*D*'  #user was pone and now dealer
            
    if game.computer_hand[0] == '*D*': #if computer was dealer
        game.computer_hand[0] = '#'    #computer is now pone
    else:
        game.computer_hand[0] = '*D*'  #if computer was pone now dealer
    r.shuffle(game.deck)
    r.shuffle(game.deck)
    r.shuffle(game.deck)
    #print('\n *#*#*#*Next Round*#*#*#*')
    game.phase = 'FINISH'
        #game.handages.append('*#*#*#*Next Round*#*#*#*')
        #stats.write(str(roundn) + ',' + str(pa_point) + ',' + str(a_point-pa_point) + '\n')
        #stats.close()
    return None
    
def analyze_3(player_tot, p_hand:list): #No print statemnts (for mogging)
    #colors first 
    red = False
    blk = False
    rc = 0
    bc = 0
    v_hand = []
    c_hand = []
    dp = None
    str_pri = None
    str_pair = None
    for card in p_hand:
        info = card.split()
        v_hand.append(info[0])  #value
        c_hand.append(info[2])  #suit "color"
    for card in c_hand:
        if card == 'Diamonds'  or card == 'Hearts':
            red = True
            rc += 1
        if card == 'Blank':
            pass
        else: #'Clubs' in card or 'Spades' in card: #else 
            blk = True  
            bc += 1
    suit_c = c_hand[0]
    if red == True and blk == True: 
        pass #keep going
    elif (red == True and blk == False) or (red == False and blk == True):  #All red/black cards
        if all(suit_c == card for card in c_hand) == True: #All same suit 
            player_tot += 6
        elif sum(suit_c == card for card in c_hand) == 3:   #3 cards same suit 
            player_tot += 5
        elif sum(suit_c == card for card in c_hand) == 2:    #2 cards in same suit 
            player_tot += 4
    elif c_hand.count(suit_c) == 3: #3 cards same suit & NOT ALL same color 
        player_tot += 3
    elif (red == True and bc == 1):     #3 in Color
        player_tot += 2
    elif (blk == True and rc == 1):  
        player_tot += 2
    #nobs and duces second
    for i in range(len(v_hand[0:3])):
        if v_hand[i] == 'Jack' and c_hand[i] == c_hand[-1]: #suit of the jack matches the suit of turned up card
            player_tot += 4
        elif v_hand[i] == '2' and c_hand[i] == c_hand[-1]:  #suit of the deuce matches the suit of turned up card
            player_tot += 4
        elif v_hand[i] == 'Jack' or v_hand[i] == '2':
            player_tot += 2
        else:
            pass
    #pairs third
    pp_hand = p_hand.copy()
    for card in pp_hand:
        cind = pp_hand.index(card)
        vitals = card.split(' ')
        pp_hand[cind] = vitals[0]
    if pp_hand[0] == pp_hand[1] == pp_hand[2] == pp_hand[3]:
        player_total += 18
        dp = str(pp_hand[0])
    for prial in it.combinations(pp_hand, 3):
        if prial[0] == prial[1] == prial[2]:
            str_pri = str(prial[0])
            if str_pri == dp:
                break
            player_tot += 9
    for pair in it.combinations(pp_hand, 2):
        if pair[0] == pair [1]:
            str_pair = str(pair[0])
            if str_pair == str_pri:     #should stop a lesser pair from being counted from the same trips
                break
            player_tot += 2
    #addition fifth
    add_hand = p_hand.copy()
    tenxs = []
    for card in add_hand:
        if 'Jack' in card[0:4] or 'Quee' in card[0:4] or 'King' in card[0:4] or '10' in card[0:2]:
            findx = add_hand.index(card)
            tenxs.append(findx)
    counter = 0
    #make cards in their numerical values for counting 
    add_hand = s.addition(add_hand)
    #If ALL 4 cards add a Number
    if sum(add_hand) == 15 or sum(add_hand) == 25 or sum(add_hand) == 31:
        player_tot += 4
        if 0 in add_hand:
            player_tot -= 1
    #The summation of three cards can ONLY equal 15 or 25 
    for triple in it.combinations(add_hand, 3):
        if sum(triple) == 15 or sum(triple) == 25:
            if 10 in triple and len(tenxs) > 1:
                #kick = p_hand[tenxs[counter]]
                counter += 1
            elif 10 in triple and len(tenxs) == 1:
                #kick = p_hand[tenxs[0]]
                pass
            else: 
                pass
            player_tot += 3
            if 0 in triple:
                player_tot -= 1
    counter = 0
    #The summation of any two cards can only equal 15
    for combo in it.combinations(add_hand, 2):
        if sum(combo) == 15:
            if 10 in combo and len(tenxs) == 1:  #works with having one 10 card and multiple othe fifteens
                #kick = p_hand[tenxs[0]]   #counter == 0
                pass
            elif 10 in combo and len(tenxs) > 1: #works with multiple 10s 
                #kick = p_hand[tenxs[counter]]
                counter += 1
            else: 
                pass
            player_tot += 2
    counter = 0
    return player_tot