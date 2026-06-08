import random
import itertools as it
import costly as c 
import strategy as s 
#hearts and 

#we can either hard wire or make this more general 
def analyze_2(player_tot, p_hand:list):
    #colors first 
    red = True 
    blk = False
    rc = 0
    bc = 0
    v_hand = []
    c_hand = []
    for card in p_hand:
        info = card.split(' ')
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
            print('Costly Colours! (4 ' + suit_c + '): +6' )
        elif sum(suit_c == card for card in p_hand) == 3:   #3 cards same suit 
            player_tot += 5
            print('4 in Colour, 3 in Suit (' + suit_c + '): +5')
        elif sum(suit_c == card for card in p_hand) == 2:    #2 cards in same suit 
            player_tot += 4
            print('4 in Colour, 2 in Suit (' + suit_c + '): +4')
    elif c_hand.count(suit_c) == 3: #3 cards same suit & NOT ALL same color 
        player_tot += 3
        print('3 in Suit (' + suit_c + '): +3') 
    elif (red == True and bc == 1):     #3 in Color
        player_tot += 2 
        print('3 in Color (Red): +2')
    elif (blk == True and rc == 1):   
        print('3 in Color (Black): +2')          
        
    #nobs and duces second
    for i in range(len(v_hand)):
        if v_hand[i] == 'Jack' and c_hand[i] == c_hand[-1]:
            player_tot += 4
            print('His Nobs: +4')
        elif v_hand[i] == '2' and c_hand[i] == c_hand[-1]:
            player_tot += 4
            print('Right Deuce: +4')
        elif v_hand[i] == 'Jack' or v_hand[i] == '2':
            player_tot += 2
            print('Jack or Duece in Hand: +2')
        else:
            pass

    #pairs third
    #make cards just their value: 'King' or '5'
    for card in p_hand:
        cind = p_hand.index(card)
        vitals = card.split(' ')
        p_hand[cind] = vitals[0]

    for pair in it.combinations(p_hand, 2):
        if pair[0] == pair [1]:
            player_tot += 2
            str_pair = str(pair[0])
            print('Pair of ' + str_pair + ': +2')
    for prials in it.combinations(p_hand, 3):
        if pair[0] == pair[1] == pair[2]:
            player_tot += 9
            str_pri = str(pair[0])
            print('Prial of ' + str_pri + ': +9')

    #sequences fourth
    seq_hand = p_hand.copy()
    value, seq_hand, ordered = s.sequence(seq_hand)     #p_hand is now just card values
    
    #addition fifth
    add_hand = s.addition(p_hand)
    
