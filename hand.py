import random
import itertools as it
import costly as c 
import strategy as s 
import time as t
#hearts and 
#we can either hard wire or make this more general 
def analyze_2(player_tot, p_hand:list):
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
    suit_c = c_hand[0]
    if red == True and blk == True: 
        pass #keep going
    elif (red == True and blk == False) or (red == False and blk == True):  #All red/black cards
        if all(suit_c == card for card in c_hand) == True: #All same suit 
            player_tot += 6
            print('Costly Colours! (4 ' + suit_c + '): +6 \n' )
        elif sum(suit_c == card for card in c_hand) == 3:   #3 cards same suit 
            player_tot += 5
            print('4 in Colour, 3 in Suit (' + suit_c + '): +5 \n')
        elif sum(suit_c == card for card in c_hand) == 2:    #2 cards in same suit 
            player_tot += 4
            print('4 in Colour, 2 in Suit (' + suit_c + '): +4 \n')
    elif c_hand.count(suit_c) == 3: #3 cards same suit & NOT ALL same color 
        player_tot += 3
        print('3 in Suit (' + suit_c + '): +3') 
    elif (red == True and bc == 1):     #3 in Color
        player_tot += 2 
        print('3 in Color (Red): +2 \n')
    elif (blk == True and rc == 1):   
        print('3 in Color (Black): +2 \n')          
        
    #nobs and duces second
    for i in range(len(v_hand[0:3])):
        if v_hand[i] == 'Jack' and c_hand[i] == c_hand[-1]: #suit of the jack matches the suit of turned up card
            player_tot += 4
            print('His Nobs: +4 \n')
        elif v_hand[i] == '2' and c_hand[i] == c_hand[-1]:  #suit of the deuce matches the suit of turned up card
            player_tot += 4
            print('Right Deuce: +4 \n')
        elif v_hand[i] == 'Jack' or v_hand[i] == '2':
            player_tot += 2
            print('Jack or Duece in Hand: +2 \n')
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
        print('Double Prial (4-of-a-kind) of ' + dp + 's: +18 \n')

    for prial in it.combinations(pp_hand, 3):
        if prial[0] == prial[1] == prial[2]:
            str_pri = str(prial[0])
            if str_pri == dp:
                break
            player_tot += 9
            print('Prial of ' + str_pri + 's: +9 \n')

    for pair in it.combinations(pp_hand, 2):
        if pair[0] == pair [1]:
            str_pair = str(pair[0])
            if str_pair == str_pri:     #should stop a lesser pair from being counted from the same trips
                break
            player_tot += 2
            print('Pair of ' + str_pair + 's: +2 \n')
    
    #sequences fourth       SEQUENCES DON'T COUNT IN HAND
    #seq_hand = p_hand.copy()    
    #true_seq = False
    #portion = seq_hand[0:2]
    ######
    #true_seq, sh, ord = s.sequence(portion) #this must be true -----  #p_hand is now just card values
    #if true_seq == False:
    #    pass
    #else: 
    #    if true_seq == True:    #the three cards dealt in hand = a run
    #        value, seq_hand, ordered = s.sequence(seq_hand)
    #        if value == True and true_seq == True:
    #            player_tot += len(seq_hand) 
    #            run = str(len(seq_hand))
    #        elif true_seq == True and value == False: 
    #            player_tot += len(portion)
    #            run = str(len(portion))
    #        print('Run of ' + run + ': +' + run +'\n')
            

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
        print('All 4 cards = ' + str(sum(add_hand)) + ': +4 \n')
    
    #The summation of three cards can ONLY equal 15 or 25 
    for triple in it.combinations(add_hand, 3):
        if sum(triple) == 15 or sum(triple) == 25:
            if 10 in triple and len(tenxs) > 1:
                kick = p_hand[tenxs[counter]]
                print(triple, end='')
                print(' -------> ' + kick)
                counter += 1
            elif 10 in triple and len(tenxs) == 1:
                kick = p_hand[tenxs[0]]
                print(triple, end='')
                print(' -------> ' + kick)
            else: 
                print(triple)
            player_tot += 3
            print('Sum to ' + str(sum(triple)) + ': +3 \n')
    counter = 0

    #The summation of any two cards can only equal 15
    for combo in it.combinations(add_hand, 2):
        if sum(combo) == 15:
            if 10 in combo and len(tenxs) == 1:  #works with having one 10 card and multiple othe fifteens
                kick = p_hand[tenxs[0]]   #counter == 0 
                print(combo, end='')
                print(' -------> ' + kick)
            elif 10 in combo and len(tenxs) > 1: #works with multiple 10s 
                kick = p_hand[tenxs[counter]]
                print(combo, end='')
                print(' -------> ' + kick)
                counter += 1
            else: 
                print(combo)
            player_tot += 2
            print('Sum to 15: +2 \n')
    counter = 0

    return player_tot

def round_totals(user_total, comp_total, pa, pb):
    print('*#*#*Round Toals*#*#*')
    
    ut = str(user_total)  #useer
    ct = str(comp_total)
    pas = str(pa)         #user's pegging
    pbs = str(pb)
    #Computer Hand
    print('---Mr. Crib---')
    print("Pegging = " + pbs)
    print("Hand = " + str(comp_total - pb))
    print("Mr. Crib's Total = " + ct + "\n")

    #user
    print('---You---') 
    print('Pegging = ' + pas)
    print("Hand = " + str(user_total - pa))
    print('Your Total = ' + ut)

