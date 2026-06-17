import random
import strategy as s
import hand as h
import time as t 

suits = ["Diamonds", "Hearts", "Clubs", "Spades", ]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

a = [] #user's hand
b = [] #computer's hand 
ah = []
bh = []
total = [] #list of card values w/o suits as strings e.g. []'7', 'Jack'] that have been played
ntotal = [] #list of card values as integers 

def cards():
    deck = []
    for suit in suits:  #for every suit
        for rank in ranks:   #going through every number assign the suit to this number 
            card = rank + ' of ' + suit
            deck.append(card)
    return deck
        
def start(deck:list):
    #shuffle the deck of cards
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    index_a = random.randint(0, 51)  #find index for picking a cut in the deck
    index_b = random.randint(0, 50)
    a_deal = deck.pop(index_a)       #take out a cut 
    b_deal = deck.pop(index_b)          
    cuts = [a_deal, b_deal]          #save cut card strings to a list 
    deck.append(a_deal)              #return cut cards to the deck 
    deck.append(b_deal)      
    for x in range(len(cuts)):                #comapre who has the lower cut 
        item = cuts[x]
        if item[0:4] == 'Jack' or item[0:4] == "King" or item[0:4] == "Quee":
            cuts[x] = int(10) 
        elif item[0:3] == 'Ace':
            cuts[x] = int(1)
        elif item[0:2] == '10':
            cuts[x] = int(10)
        else: 
            cuts[x] = int(item[0])
    if cuts[0] < cuts[1]:
        a.append('*D*')
        b.append('#')
    else: 
        b.append('*D*')
        a.append('#')
    random.shuffle(deck)
    return deck

def deal(deck:list): 
    #"deal the cards" by popping the first item of the deck list
    for i in range(6):
        hand = deck.pop(0)
    #put that item (card) into the alternating lists of a and b 
        if b[0] == '*D*':  #if computer is dealer deal to user first
            if i % 2 != 0:
                b.append(hand)
            else: 
                a.append(hand)
        elif b[0] == '#':   #if user is the dealer
            if i % 2 != 0:
                a.append(hand)
            else: 
                b.append(hand)
    #make the deck card 
    top = deck.pop(0) 
    top_card = "Top card is: " + top 
#print the list that a (user) has 
    print(a)
    print(top_card)
    print('')
    return top

def analyze(c_card:str, player_total):
    numadd = 0 
    vitals = c_card.split(' ') #list with ['#', 'of', 'suit']
    #add to running total pile
    total.append(vitals[0])  #string value (no suit) stays in total 
    #analyze running total function
  #pairs first 
    if len(total) >= 4 and total[-4] == total[-3] == total[-2] == total[-1]:
        player_total += 18
        numadd += 18
        print('Double Prial (4-of-a-kind) +18')
    elif len(total) >= 3 and total[-3] == total[-2] == total[-1]:
        player_total += 9 
        numadd += 9
        print('Prial (3-of-a-kind) +9')
    elif len(total) >= 2 and total[-2] == total[-1]:
        player_total += 2
        numadd += 2
        print('Pair +2')

  #sequence second 
    #ordtotal = sorted(total, key=ranks.index) #sorted total sequence strings 
    if len(total) >= 3:
        true_seq = False
        portion = total[-3:]
        ######
        true_seq, sh, ord = s.sequence(portion) #this must be true 
        p_ind = -4
        if true_seq == False:
            pass
        else: 
            while true_seq == True and (abs(p_ind) <= len(total)):
                portion = total[p_ind:]
                true_seq, sh, ord = s.sequence(portion)
                p_ind = p_ind - 1

            if true_seq == True:
                player_total += len(portion)
                run = str(len(portion))
                print('Run of ' + run + ': +' + run)
            elif true_seq == False and len(portion) >= 3: 
                p_ind = p_ind +2 
                portion = total[p_ind:]
                player_total += len(portion)
                run = str(len(portion))
                print('Run of ' + run + ': +' + run)
    else: 
        pass    
    #change face cards to numbers of summation points 
    if vitals[0] == 'Jack' or vitals[0] == "Queen" or vitals[0] == "King" :
        vitals[0] = 10
    elif vitals[0] == 'Ace':
        vitals[0] = 1
    else:
        vitals[0] = int(vitals[0])
    ntotal.append(vitals[0])

  #sums third 
    if sum(ntotal) == 31:
        snumadd = len(ntotal)
        player_total += snumadd
        print('31 +' + str(snumadd))   #add a line making total and ntotal 0
        numadd += snumadd
        total.clear()
    elif sum(ntotal) == 25:
        snumadd = len(ntotal)
        player_total += snumadd
        print('25 +' + str(snumadd))
        numadd += snumadd
    elif sum(ntotal) == 15:
        snumadd = len(ntotal)
        player_total += snumadd
        print('15 +' + str(snumadd))
        numadd += snumadd
    return player_total, sum(ntotal)
    
#Pegging playCard Turn 
def initial(top:str):
    a_points = int(0)
    b_points = int(0)
    #if top card is Jack or Deuce add 4 points to dealer of 'His Heels'
    top_type = top[0:4]
    if top_type == 'Jack':
        if a[0] == '*D*':
            a_points += 4
            print('His Heels +4')
        else:
            b_points += 4
            print('Mr. Crib: His Heels +4')
    if top_type == '2 of':
        if a[0] == '*D*':
            a_points += 4
            print('Duece Down +4')
        else:
            b_points += 4
            print('Mr. Crib: Duece Down +4')
    return a_points, b_points
    
def go(signal, player_tot): 
    if signal == 0: 
        total.clear()
        ntotal.clear()
        player_tot += 1 
        print('Go! +1 for Mr. Crib \n')
    elif signal == None: 
        total.clear()
        ntotal.clear()
        player_tot += 1
        print('Go! +1 for you \n')
    return player_tot

def user_error(chosen):
    #If the typed value is not an integer
    while True:
        try:
            chosen = int(chosen)
            break
        except ValueError: 
            chosen = input('Type an integer (0, 1, 2, or , 3): ')
    #If chosen number is not in the list of cards by size (1,2,3 or 0)
    if chosen > len(a) - 1:
        print('**Out of Position** -- Choose the correct card position \n')
        chosen = input("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
        rechoose = chosen
        return user_error(rechoose)
    #If player tries to Renege
    if chosen == 0:
        rtest = a.copy()
        for card in rtest[1:]:
           cix = rtest.index(card)
           if card[0:4] == 'Jack' or card[0:4] == 'Quee' or card[0:4] == 'King' or card[0:2] == '10':
                rtest[cix] = 10
           elif card[0:3] == 'Ace':
                rtest[cix] = 1
           else:
                rtest[cix] = int(card[0])

        for card in rtest[1:]:
            cix = rtest.index(card)
            if card + sum(ntotal) <= 31: ###A renege 
                print('**Renege** - You can still play a card (' + str(a[cix]) + ') with Total remaining under 31')  
                rechoose = input('Choose the correct card 1 or 2: ')
                print('')
                return user_error(rechoose)

    v_spl = a[chosen].split()
    if v_spl[0] == 'Jack' or v_spl[0] == 'Queen' or v_spl[0] == 'King':
        v_spl[0] = 10
    elif v_spl[0] == 'Ace':
        v_spl[0] = 1
    elif v_spl[0] == '#' or v_spl[0] == '*D*':  #indication of a go by the player
        return 0
    numb = int(v_spl[0])
    #If player Has to say go, but tries to play a card
    if sum(ntotal) + numb > 31:
        #while sum(ntotal) + numb > 31:
        print('**Over 31** --- Choose a differnet card or type "0" for Go \n')
        rechoose = input("Selection: ")
        return user_error(rechoose)
            #if a person picks a number out of the card hand range 
        if rechoose > len(a) - 1:
            while rechoose > len(a) - 1:
                print('**Out of Position** -- Choose the correct card position \n')
                rechoose = int(input("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): "))
            #turn chosen card into numerical value 
        v_spl = a[rechoose].split()
        if v_spl[0] == 'Jack' or v_spl[0] == 'Queen' or v_spl[0] == 'King':
            v_spl[0] = 10
        elif v_spl[0] == 'Ace':
            v_spl[0] = 1
            #Once a go is correctly declared
        elif v_spl[0] == '#' or v_spl[0] == '*D*':
            #break
        #else:
            numb = int(v_spl[0])
    else:
        rechoose = chosen 
    return rechoose
 
#Mogging
def mogging(a_tot, b_tot, trumper, ag_tot):
# Dealer has the right to mog first = offer up a card to give to dealer
    if a[0] == '*D*':
        mog = input('Would you like to "Mog" (trade a card with Mr. Crib). Type Y or N:')
        while mog not in ('Y', 'N'):
            mog = input("Please just type capital 'Y' for yes, or capital 'N' for No: ")
        cmog, card_choice = s.mog_choice(b[1:], trumper, ag_tot)
        #   allow the computer to decide if it would like to mog
        #   save the computer choice as cmog
        if mog == 'Y' and cmog == 'N':
            a_tot += 1
            print(cmog + 'o --------------> Mr. Crib refuses to Mog: +1 point')
            print("")
        elif mog == 'N':
            b_tot += 1
            print('You refuse to Mog: Mr.Crib +1 point')
            print("") 
        elif mog == 'Y' and cmog == 'Y':
            print("Mr. Crib also wishes to Mog!")
            trade = input('Select the card you wish to trade (1, 2, or 3): ') 
            trade = user_error(trade)
            trade = int(trade)
            crade = b.index(card_choice) #computer selects the card they want to get rid of 
            t_card = a.pop(trade)
            tc_card = b.pop(crade)
            a.append(tc_card)
            b.append(t_card)
            print("Your hand is now:")
            print(a)
            print("")
    else:
        cmog, card_choice = s.mog_choice(b[1:], trumper, ag_tot)
        if cmog == 'N':
            a_tot += 1
            #print(cmog + 'o -------------->')
            print("Mr. Crib refuses to Mog: +1 point\n")
        elif cmog == 'Y':  
            print("Mr. Crib wants to Mog")
            mog = input("Would you like to 'Mog' (trade a card to Mr. Crib). Type Y or N: ")
            while mog not in ('Y', 'N'):
                mog = input("\n***Please just type capital 'Y' for yes, or capital 'N' for No: ")
            if mog == 'N':
                b_tot += 1
                print("You refuse to Mog: Mr.Crib +1 point\n")
            elif mog == 'Y':
                print("You also wish to Mog!")
                trade = input('Select the card you wish to trade (1, 2, or 3): ') 
                trade = user_error(trade)
                trade = int(trade)
                crade = b.index(card_choice) #computer selects the card they want to get rid of 
                t_card = a.pop(trade)
                tc_card = b.pop(crade)
                a.append(tc_card)
                b.append(t_card)
                print("Your hand is now:")
                print(a)
                print("")
    return a_tot, b_tot

#Pegging Play
def pegging(a_tot, b_tot, playerp:int, compp:int):
    #Non-dealer starts
    #could put this in a 'for' loop x in range(6)
    got = 'x'
    gotc = 'comp' 
    while len(a) > 1 or len(b) > 1:  
    #for inning in range(3):
        if a[0] == '#':
        #1st Play = User
            nflop = input("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ") #user enters integer of card
            
            #user error
            nflop = user_error(nflop)

            if nflop != 0:          #(run as normal)
                flop = a[nflop]
                a_tot, total_sum = analyze(flop, a_tot)
                print(flop + ' --> Total is: ' + str(sum(ntotal)))
                ###CHECK FOR WIN
                if playerp + a_tot >= 61:
                    #print("You Win off of pegging: (point total)")
                    break
                else:
                    pass
                if total_sum == 31:
                    ntotal.clear()
                    print('')
                else:
                    pass
                a.pop(nflop)
                ah.append(flop)
            elif nflop == 0 and got == 'x': #use go procedure ------------------- (User says 'go' and Starts pegging after)
            #Allow computer to make a play
                print('Go! ----->')
                cflop = s.next_card(ntotal, total, b[1:])
                if cflop == None:
                    b_tot = go(nflop, b_tot)
                    print(a)
                    continue       #Allows the user to start at the top of the loop
                else: 
                    pass #break?? / pass

            #2nd Play = Computer's choice and show
            flop = s.next_card(ntotal, total, b[1:])
            if flop != None:           #Normal Play 
                b_tot, total_sum = analyze(flop, b_tot)
                print(flop + ' --> Total is: ' + str(sum(ntotal)))
                ###CHECK FOR WIN
                if compp + b_tot >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                    break
                else:
                    pass
                if total_sum == 31:
                    ntotal.clear()
                    print('')
                else:
                    pass
                nflop = b.index(flop)
                b.pop(nflop)
                bh.append(flop)
            else: #'comp' & 0          #use go procedure ---------------
                if nflop != 0 and got == 'x': #(indicating the player hasn't reciprocated the go)
                    print('Go! ----->')
                    print(a)
                    got = 'comp'
                    continue
                elif got == 'comp':
                    a_tot = go(flop, a_tot)
                    #Computer's turn  (maybe put the computer gameplay in that part of the go)
                    seq_value, seq_hand, orderd = s.sequence(b[1:])
                    w = s.first_card_non(seq_hand, seq_value, orderd)
                    xflop = random.choices(b[1:], weights=w)
                    flop = xflop[0]
                    b_tot, total_sum = analyze(flop, b_tot)
                    print(flop + ' --> Total is: ' + str(sum(ntotal)))
                    ###CHECK FOR WIN
                    if compp + b_tot >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                        break
                    else:
                        pass
                    nflop = b.index(flop)
                    b.pop(nflop)
                    bh.append(flop)
            print(a)
        
        else: 
        #1st Play = Computer's choice
            if len(total) == 0:
                seq_value, seq_hand, orderd = s.sequence(b[1:])
                w = s.first_card_non(seq_hand, seq_value, orderd)
                xflop = random.choices(b[1:], weights=w)
                flop = xflop[0]
            else: 
                flop = s.next_card(ntotal, total, b[1:])

            if flop == None and gotc == 'x':    #user's fault and Computer can't play 
                b_tot = go(nflop, b_tot)  #Figuiring out ----------------
                pass #continue maybe
            elif flop != None:
                b_tot, total_sum = analyze(flop, b_tot)
                print(flop + ' --> Total is: ' + str(sum(ntotal)))
                ###CHECK FOR WIN
                if compp + b_tot >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                    break
                else:
                    pass
                if total_sum == 31:
                    ntotal.clear()
                    print('')
                else:
                    pass
                nflop = b.index(flop)
                b.pop(nflop)
                bh.append(flop)
            else:      #Let the user make a play 
                #Let user go 
                if nflop == 0 and gotc == 'comp':   #computer's fault 
                    #run go
                    a_tot = go(flop, a_tot)
                    continue
                else: 
                    print('Go! ----->')
                    pass

            #2nd Play = User's turn 
            print(a)
            nflop = input("Choose card # 1, 2, or 3: (If applicable type '0' for a Go):") #user enters integer of card (index)
            nflop = user_error(nflop)
            if nflop != 0:    #(run as normal)
                flop = a[nflop]  #value / card 
                a_tot, total_sum = analyze(flop, a_tot)
                print(flop + ' --> Total is: ' + str(sum(ntotal)) + '\n')
                ###CHECK FOR WIN
                if playerp + a_tot >= 61:
                    #print("You Win off of pegging: (point total)")
                    break
                else:
                    pass
                if total_sum == 31:
                    ntotal.clear()
                    print('')
                else:
                    pass
                a.pop(nflop)
                ah.append(flop)
            else: 
                if flop != None:
                    print('Go! ----->')
                    gotc = 'x'                   #go is user fault
                    pass  
                elif nflop == 0 and gotc == 'x':
                    #go procedure -------------
                    b_tot = go(nflop, b_tot)
                    nflop = input("Choose card # 1, 2, or 3: (If applicable type '0' for a Go):")
                    nflop = user_error(nflop)
                    flop = a[nflop]  #value / card 
                    a_tot, total_sum = analyze(flop, a_tot)
                    print(flop + ' --> Total is: ' + str(sum(ntotal)))
                    ###CHECK FOR WIN
                    if playerp + a_tot >= 61:
                    #print("You Win off of pegging: (point total)")
                        break
                    else:
                        pass
                    a.pop(nflop)
                    ah.append(flop)
    print('---Pegging Completed---')
    print("Mr. Crib's Points: " + str(b_tot))
    print("Your Points: " + str(a_tot))
    return a_tot, b_tot
    
    #Hand Play    

def hand(a_tot, b_tot, top_cd):
    t.sleep(2)
    print('\n---Hand Play---')
    pa_total = a_tot
    pb_total = b_tot
    ah.append(top_cd)
    bh.append(top_cd)
    print('Top Card is: ' + top_cd + '\n')
    if a[0] == '#':
        t.sleep(1.5)
        print('Non-Dealer (Your) Hand Totals:')
        #count (non-dealer) user's hand first 
        print(ah)
        a_tot = h.analyze_2(a_tot, ah)
        hatot = a_tot - pa_total
        if hatot < 0:
            hatot = 0 
        print('Your Total is: ' + str(hatot) + '\n')
        ###count (dealer) computer's hand last 
        t.sleep(1.25)
        print("Dealer's (Mr. Crib's) Hand Totals:")
        print(bh)
        b_tot = h.analyze_2(b_tot, bh)
        hbtot = b_tot - pb_total
        if hbtot < 0:
            hbtot = 0
        print("Mr. Crib's Total is: " + str(hbtot) + '\n')
    
    else:
        #count computer (non-d) first
        t.sleep(1)
        print("Non-Dealer (Mr. Crib's) Hand Totals:")
        print(bh)
        b_tot = h.analyze_2(b_tot, bh)
        hbtot = b_tot - pb_total
        if hbtot < 0:
            hbtot = 0
        print("Mr. Crib's Total is: " + str(hbtot) + '\n')
        ###user = dealer last 
        t.sleep(1.25)
        print("Dealer's (Your) Hand Totals:")
        print(ah)
        a_tot = h.analyze_2(a_tot, ah)
        hatot = a_tot - pa_total
        if hatot < 0:
            hatot = 0
        print('Your Total is: ' + str(hatot) + '\n')
    total.clear()
    ntotal.clear()
    return a_tot, b_tot
    
def return_cards(u_hand, ai_hand, topc, deck:list):
    u_hand.pop()
    for card in u_hand[0:3]:
        deck.append(card)
    ai_hand.pop()
    for card in ai_hand:
        deck.append(card)
    deck.append(topc)
    ah.clear()
    bh.clear()
    return deck

def main(): 
    main_deck = cards()
    main_deck = start(main_deck)
    print('*#*#*#*#*Costly Colours*#*#*#*#*')
    trump = deal(main_deck)
    a_point, b_point = initial(trump)
    pa_point, pb_point = pegging(a_point, b_point)
    a_point, b_point = hand(pa_point, pb_point, trump)  #total points after the round for each player
    h.round_totals(a_point, b_point, pa_point, pb_point)
    main_deck = return_cards(ah, bh, trump, main_deck)
    
if __name__ == '__main__':
    main()    

