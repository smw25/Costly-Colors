import random
import itertools as it
import costly as c 
import strategy as s 
#hearts and 

#we can either hard wire or make this more general 
def analyze_2(player_tot, p_hand:list):
    #colors first 
    for card in p_hand:
        if 'Diamonds' in card or 'Hearts' in card:
            red = True
        else: #'Clubs' in card or 'Spades' in card: #else 
            blk = True  
        
    if red == True and blk == True: 
        pass
    else: 
        pass #keep going 
    if all('Heart' in card for card in p_hand) == True:
        player_tot += 6
        print('Costly Colours! (4 Hearts): +6' )
    #nobs and duces second

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
