import random
import xstrategy as s
import xhand as h
import time as t 

suits = ["Diamonds", "Hearts", "Clubs", "Spades", ]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

a = [] #user's hand
b = [] #computer's hand 
ah = []
bh = []
total = [] #list of card values w/o suits as strings e.g. []'7', 'Jack'] that have been played
ntotal = [] #list of card values as integers 

def cards(game):
    #game.deck = []
    for suit in suits:  #for every suit
        for rank in ranks:   #going through every number assign the suit to this number 
            card = rank + ' of ' + suit
            game.deck.append(card)
    #return game.deck
        
def start(game): #deck:list
    #shuffle the deck of cards
    name = '*#*#*#*#*Costly Colours*#*#*#*#*'
    random.shuffle(game.deck)
    random.shuffle(game.deck)
    random.shuffle(game.deck)
    index_a = random.randint(0, 51)  #find index for picking a cut in the deck
    index_b = random.randint(0, 50)
    a_deal = game.deck.pop(index_a)       #take out a cut 
    b_deal = game.deck.pop(index_b)          
    cuts = [a_deal, b_deal]          #save cut card strings to a list 
    game.deck.append(a_deal)              #return cut cards to the deck 
    game.deck.append(b_deal)      
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
        game.player_hand.append('*D*')
        game.computer_hand.append('#')
    else: 
        game.computer_hand.append('*D*')
        game.player_hand.append('#')
    random.shuffle(game.deck)
    return name

def win(game):
    if game.player_score + game.player_rsco >= 61:
        game.player_score += game.player_rsco
        game.phase = "GAME_OVER"
        game.winner = "PLAYER"
        game.wintags.append('*#*#*#*#*#*#* GAME OVER *#*#*#*#**#*#*')
        game.wintags.append("🎉You win!🎉 with a total of " + str(game.player_score))
        return True 
    elif game.computer_score + game.comp_rsco >= 61:
        game.computer_score += game.comp_rsco
        game.phase = "GAME_OVER"
        game.winner = "COMPUTER"
        game.wintags.append('*#*#*#*#*#*#* GAME OVER *#*#*#*#**#*#*')
        game.wintags.append("Mr. Crib Wins with a total of " + str(game.computer_score))
        return True
    return False

def deal(game): #deck:list
    #"deal the cards" by popping the first item of the deck list
    for i in range(6):
        hand = game.deck.pop(0)
    #put that item (card) into the alternating lists of a and b 
        if game.computer_hand[0] == '*D*':  #if computer is dealer deal to user first
            if i % 2 != 0:
                game.computer_hand.append(hand)
            else: 
                game.player_hand.append(hand)
        elif game.computer_hand[0] == '#':   #if user is the dealer
            if i % 2 != 0:
                game.player_hand.append(hand)
            else: 
                game.computer_hand.append(hand)
    #make the deck card 
    top = game.deck.pop(0) 
    top_card = "Top card is: " + top 
#print the list that a (user) has 
    #print(a)
    game.messages.append(game.player_hand.copy())
    #print(top_card)
    game.messages.append(top_card)
    #print('')
    game.top = top
    return game

def analyze(c_card:str, player_total, game):   #game.player_rsco OR game.comp_rsco
    numadd = 0 
    vitals = c_card.split(' ') #list with ['#', 'of', 'suit']
    #add to running total pile
    game.running_cards.append(vitals[0])  #string value (no suit) stays in total 
    #analyze running total function
  #pairs first 
    if len(game.running_cards) >= 4 and game.running_cards[-4] == game.running_cards[-3] == game.running_cards[-2] == game.running_cards[-1]:
        player_total += 18
        numadd += 18
        #print('Double Prial (4-of-a-kind) +18')
        game.messages.append('Double Prial (4-of-a-kind) +18')
    elif len(game.running_cards) >= 3 and game.running_cards[-3] == game.running_cards[-2] == game.running_cards[-1]:
        player_total += 9 
        numadd += 9
        #print('Prial (3-of-a-kind) +9')
        game.messages.append('Prial (3-of-a-kind) +9')
    elif len(game.running_cards) >= 2 and game.running_cards[-2] == game.running_cards[-1]:
        player_total += 2
        numadd += 2
        #print('Pair +2')
        game.messages.append('Pair +2')

  #sequence second 
    #ordtotal = sorted(total, key=ranks.index) #sorted total sequence strings 
    if len(game.running_cards) >= 3:
        true_seq = False
        portion = total[-3:]
        ######
        best_run = 0
    # Check from longest possible slice down to 3
        for run_len in range(len(game.running_cards), 2, -1):       #(start, stop, step)
            portion = game.running_cards[-run_len:]
            true_seq, sh, ord = s.sequence(portion)
            if true_seq == True:
                best_run = run_len
                break  # longest run found, stop

    #if best_run >= 3:
    #    player_total += best_run
    #    print('Run of ' + str(best_run) + ': +' + str(best_run))
        ######
        #true_seq, sh, ord = s.sequence(portion) #this must be true 
        #p_ind = -4
        if true_seq == False:
            pass
        else: 
            #while true_seq == True and (abs(p_ind) <= len(total)):
            #    portion = total[p_ind:]
            #    true_seq, sh, ord = s.sequence(portion)
            #    p_ind = p_ind - 1

            if true_seq == True:
                player_total += len(portion)
                run = str(len(portion))
                #print('Run of ' + run + ': +' + run)
                game.messages.append('Run of ' + run + ': +' + run)
            #elif true_seq == False and len(portion) >= 3: 
                #p_ind = p_ind +2 
                #portion = total[p_ind:]
                #player_total += len(portion)
                #run = str(len(portion))
                #print('Run of ' + run + ': +' + run)
    else: 
        pass    
    #change face cards to numbers of summation points 
    if vitals[0] == 'Jack' or vitals[0] == "Queen" or vitals[0] == "King" :
        vitals[0] = 10
    elif vitals[0] == 'Ace':
        vitals[0] = 1
    else:
        vitals[0] = int(vitals[0])
    game.running_values.append(vitals[0])

  #sums third 
    if sum(game.running_values) == 31:
        snumadd = len(game.running_values)
        player_total += snumadd
        #print('31 +' + str(snumadd))   #add a line making total and ntotal 0
        game.messages.append('31 +' + str(snumadd))
        numadd += snumadd
        game.running_cards.clear()
    elif sum(game.running_values) == 25:
        snumadd = len(game.running_values)
        player_total += snumadd
        #print('25 +' + str(snumadd))
        game.messages.append('25 +' + str(snumadd))
        numadd += snumadd
    elif sum(game.running_values) == 15:
        snumadd = len(game.running_values)
        player_total += snumadd
        #print('15 +' + str(snumadd))
        game.messages.append('15 +' + str(snumadd))
        numadd += snumadd
    
    #adding '1 for the latter' 
    if len(game.player_hand) == 2 and len(game.computer_hand) == 1 and sum(game.running_values) != 31:
        #if c_card in game.player_hand:
            player_total += 1
            #print('+1 For the "Latter"')
            game.messages.append('+1 For the "Latter"')
            game.phase = 'END_PEG'
    if len(game.computer_hand) == 2 and len(game.player_hand) == 1 and sum(game.running_values) != 31:
        #if c_card in game.computer_hand:
            player_total += 1
            #print('+1 For the "Latter"')
            game.messages.append('+1 For the "Latter"')
            game.phase = 'END_PEG'
    return player_total, sum(game.running_values)
    
#Pegging playCard Turn 
def initial(game): #top:str
    a_points = int(0)
    b_points = int(0)
    #game.messages.clear()
    top = game.top
    #if top card is Jack or Deuce add 4 points to dealer of 'His Heels'
    top_type = top[0:4]
    if top_type == 'Jack':
        if game.player_hand[0] == '*D*':
            a_points += 4
            #print('His Heels +4')
            game.messages.append('His Heels +4')
        else:
            b_points += 4
            #print('Mr. Crib: His Heels +4')
            game.messages.append('Mr. Crib: His Heels +4')
        win(game)
    if top_type == '2 of':
        if game.player_hand[0] == '*D*':
            a_points += 4
            #print('Duece Down +4')
            game.messages.append('Duece Down +4')
        else:
            b_points += 4
            #print('Mr. Crib: Duece Down +4')
            game.messages.append('Mr. Crib: Duece Down +4')
        win(game)
    game.player_rsco += a_points
    game.comp_rsco += b_points
    return game
    
def go(signal, player_tot, game): 
    if signal == 0: 
        #total.clear()
        game.running_cards.clear()
        #ntotal.clear()
        game.running_values.clear()
        game.go = "None"
        player_tot += 1 
        #print('Go! +1 for Mr. Crib \n')
        game.messages.append('Go! +1 for Mr. Crib')
        game.messages.append('')
        #game.messages.append(game.player_hand)
    elif signal == None: 
        #total.clear()
        game.running_cards.clear()
        #ntotal.clear()
        game.running_values.clear()
        player_tot += 1
        game.go = "None"
        #print('Go! +1 for you \n')
        game.messages.append('Go! +1 for you')
    return player_tot

def user_error(chosen, game):
    chosen = int(chosen)
    #If the typed value is not an integer
    #chosen = int(chosen)
    #----------NOT NEEDED WITH WEBSITE------------#
    #while True:
    #    try:
    #        chosen = int(chosen)
    #        break
    #    except ValueError: 
    #        chosen = input('Type an integer (0, 1, 2, or , 3): ')
    #---------------------------------------------------#
    
    #If chosen number is not in the list of cards by size (1,2,3 or 0) 
    if chosen > len(game.player_hand) - 1:
        #print('**Out of Position** -- Choose the correct card position \n')
        game.messages.append('**Out of Position** -- Choose the correct card position')
        #chosen = input("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
        game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
        return False
        rechoose = chosen   #------Not needed for website------#
        return user_error(rechoose)
    #If player tries to Renege
    if chosen == 0:
        rtest = game.player_hand.copy()
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
            if card + sum(game.running_values) <= 31: ###A renege 
                #print('**Renege** - You can still play a card (' + str(game.player_hand[cix]) + ') with Total remaining under 31')  
                game.messages.append('**Renege** - You can still play a card (' + str(game.player_hand[cix]) + ') with Total remaining under 31')
                #rechoose = input('Choose the correct card 1 or 2: ')
                game.messages.append('Choose the correct card 1 or 2: ')
                #print('')
                return False #user_error(rechoose)

    v_spl = game.player_hand[chosen].split()
    if v_spl[0] == 'Jack' or v_spl[0] == 'Queen' or v_spl[0] == 'King':
        v_spl[0] = 10
    elif v_spl[0] == 'Ace':
        v_spl[0] = 1
    elif v_spl[0] == '#' or v_spl[0] == '*D*':  #indication of a go by the player
        return 0
    numb = int(v_spl[0])

    #If player Has to say go, but tries to play a card
    if sum(game.running_values) + numb > 31:
        #while sum(ntotal) + numb > 31:
        #print('**Over 31** --- Choose a differnet card or type "0" for Go \n')
        game.messages.append('**Over 31** --- Choose a differnet card or type "0" for Go')
        #rechoose = input("Selection: ")
        game.messages.append("Selection: ")
        #return user_error(rechoose)
            #if a person picks a number out of the card hand range 
        return False
    else:
        rechoose = chosen 
    return rechoose

def mog_choice(game, inp): #NO RETURNS
    mog = inp
    if game.player_hand[0] == '#':
        cmog, game.card_choice = s.mog_choice(game.computer_hand[1:], game.top, game.player_score)
        if mog == 'Y' and cmog == 'N':
            game.player_rsco += 1
            game.phase = 'PEG_START'
            #print(cmog + 'o --------------> Mr. Crib refuses to Mog: +1 point\n')
            game.messages.append(cmog + 'o --------------> Mr. Crib refuses to Mog: +1 point')
            #print("")
            game.messages.append(" ")
        elif mog == 'N':
            game.comp_rsco += 1
            game.phase = 'PEG_START'
            #print('You refuse to Mog: Mr.Crib +1 point\n')
            game.messages.append('You refuse to Mog: Mr.Crib +1 point')
            #print("")
            game.messages.append(" ")   
        elif mog == 'Y' and cmog == 'Y':
                game.phase = "MOGGING"
                    #print("Mr. Crib also wishes to Mog!")
                game.messages.append("Mr. Crib also wishes to Mog!")
                    #trade = input('Select the card you wish to trade (1, 2, or 3): ') 
                game.messages.append('Select the card you wish to trade (1, 2, or 3): ')

    else:   #player is the dealer
        cmog, game.card_choice = s.mog_choice(game.computer_hand[1:], game.top, game.player_score)
        if cmog == 'N':
            game.player_rsco += 1
            game.phase = 'PEG_START'
            ####print(cmog + 'o -------------->')
            #print("Mr. Crib refuses to Mog: +1 point\n")
            game.messages.append("Mr. Crib refuses to Mog: +1 point")
            return game
        elif cmog == 'Y':  
            #print("Mr. Crib wants to Mog")
            game.messages.append("Mr. Crib wants to Mog")
            #mog = input("Would you like to 'Mog' (trade a card to Mr. Crib). Type Y or N: ")
            #while mog not in ('Y', 'N'):
            #    mog = input("\n***Please just type capital 'Y' for yes, or capital 'N' for No: ")
            if mog == 'N':
                game.comp_rsco += 1
                game.phase = 'PEG_START'
                #print("You refuse to Mog: Mr.Crib +1 point\n")
                game.messages.append("You refuse to Mog: Mr.Crib +1 point")  
            elif mog == 'Y':
                game.phase = "MOGGING"
                #print("You also wish to Mog!")
                game.messages.append("You also wish to Mog!")
                #trade = input('Select the card you wish to trade (1, 2, or 3): ')
                game.messages.append('Select the card you wish to trade (1, 2, or 3): ') 
    #game.card_choice = card_choice
    #game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
    return game
           
#Mogging ---- NO RETURNS
def mogging(game, trd, card_choice): #local user total, local computer total, trump card, user grand total
# Dealer has the right to mog first = offer up a card to give to dealer
    game.phase = "MOGGING"
    if game.player_hand[0] == '#':
        #trade = user_error(trd, game)
        trade = int(trd)
        crade = game.computer_hand.index(card_choice) #computer selects the card they want to get rid of 
        t_card = game.player_hand.pop(trade)
        tc_card = game.computer_hand.pop(crade)
        game.player_hand.append(tc_card)
        game.computer_hand.append(t_card)
        #print("Your hand is now:")
        game.messages.append("Your hand is now:")
        #print(a)
        game.messages.append(game.player_hand)
        #print("")
        game.messages.append("")
        game.phase = "PEG_START"
        game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
    else: 
        #trade = user_error(trd, game)
        trade = int(trd)
        crade = game.computer_hand.index(card_choice) #computer selects the card they want to get rid of 
        t_card = game.player_hand.pop(trade)
        tc_card = game.computer_hand.pop(crade)
        game.player_hand.append(tc_card)
        game.computer_hand.append(t_card)
        #print("Your hand is now:")
        game.messages.append("Your hand is now:")
        #print(a)
        game.messages.append(game.player_hand)
        #print("")
        game.messages.append("")
        game.phase = "PEG_START"
    #game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
    return game

def start_peg(game):
    #if player is non-dealer they play first 
    if game.player_hand[0] == '#':
        game.phase = 'PLAYER_TURN'
        game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")
    else:
        game.phase = 'COMP_TURN'

def player_peg(game, choice): #NO RETURN
    nflop = choice
    if nflop != 0:          #(run as normal)
        flop = game.player_hand[nflop]
        game.player_rsco, total_sum = analyze(flop, game.player_rsco, game)
        #if game.phase == "END_PEG":
        #    return
        #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
        game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
        if win(game) is True:
            return 
        ###CHECK FOR WIN
        if total_sum == 31:
            game.running_values.clear()
        else:
            pass
        game.player_hand.pop(nflop)
        game.player_played.append(flop)
    elif nflop == 0 and game.go == 'GO_C': #Computer said go and user can't play 
        nflop = None
        game.player_rsco = go(nflop, game.player_rsco, game)
    elif nflop == 0: #(got == 'x':)      #User says go 
            #Allow computer to make a play
        game.messages.append('Go! ----->')
        game.go = 'GO_P'
    game.phase = 'COMP_TURN'

def comp_peg(game): #NO RETURN
    ### First play in pegging is the computer ------CHOOSING THE CARD-----------
    if len(game.running_cards) == 0 and len(game.computer_hand) == 1: #if total is reset but computer has no more cards
        flop = None
    elif len(game.running_cards) == 0:  #total
        seq_value, seq_hand, orderd = s.sequence(game.computer_hand[1:])
        w = s.first_card_non(seq_hand, seq_value, orderd)
        xflop = random.choices(game.computer_hand[1:], weights=w)
        flop = xflop[0]      
    ### Everything besides first play ###     
    else: 
        flop = s.next_card(game.running_values, game.running_cards, game.computer_hand[1:])

    #------DELIVERING THE CARD------
    if flop == None and game.go == "GO_P": #user's fault and Computer can't play    #and gotc == 'x':
        nflop = 0
        game.comp_rsco = go(nflop, game.comp_rsco, game)  #Figuiring out ----------------
        pass #continue maybe
    elif flop == None and game.go == "None":    #Computer is first to say GO
        nflop = None
        game.go = "GO_C"
        game.messages.append('Go! ----->')
        #game.comp_rsco = go(nflop, game.comp_rsco, game)
    elif flop != None:
        game.comp_rsco, total_sum = analyze(flop, game.comp_rsco, game)
        game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
        if win(game) is True:
                    return
        if total_sum == 31:
            game.running_values.clear()
        nflop = game.computer_hand.index(flop)
        game.computer_hand.pop(nflop)
        game.computer_played.append(flop)
    else:
        pass
        #nflop = game.computer_hand.index(flop)
        #game.computer_hand.pop(nflop)
        #game.computer_played.append(flop)   

    if len(game.player_played) == 3 and len(game.computer_played) == 3:
        game.phase = 'END_PEG'
    else:
        game.phase = 'PLAYER_TURN'
        game.messages.append(game.player_hand)
        game.messages.append("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ")

def peg_stop(game):
    #if len(game.player_played) == 3 and len(game.computer_played) == 3:
        game.messages.append('------- Pegging Completed -------')
        game.messages.append("Mr. Crib's Points: " + str(game.comp_rsco))
        game.messages.append("Your Points: " + str(game.player_rsco))
        game.phase = 'HANDS'

#Pegging Play
def pegging(game, a_tot, b_tot, playerp:int, compp:int):
    #Non-dealer starts
    #could put this in a 'for' loop x in range(6)
    got = 'x'
    gotc = 'comp' 
    while len(game.player_hand) > 1 or len(game.computer_hand) > 1:  
    #for inning in range(3):
        if game.player_hand[0] == '#':
        #1st Play = User
            nflop = input("Choose card # 1, 2, or 3 (If applicable type '0' for a Go): ") #user enters integer of card
            #---Insert input from html---#
            #user error
            nflop = user_error(nflop, game)
            if nflop != 0:          #(run as normal)
                flop = game.player_hand[nflop]
                game.player_rsco, total_sum = analyze(flop, game.player_rsco)
                #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
                game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                ###CHECK FOR WIN
                if game.player_score + game.player_rsco >= 61:
                    ##print("You Win off of pegging: (point total)")
                    break
                else:
                    pass
                if total_sum == 31:
                    game.running_values.clear()
                    print('')
                else:
                    pass
                game.player_hand.pop(nflop)
                game.player_played.append(flop)
            elif nflop == 0 and got == 'x': #use go procedure ------------------- (User says 'go' and Starts pegging after)
            #Allow computer to make a play
                #print('Go! ----->')
                game.messages.append('Go! ----->')
                cflop = s.next_card(game.running_values, game.running_cards, game.computer_hand[1:])
                if cflop == None:
                    game.comp_rsco = go(nflop, game.comp_rsco)
                    #print(game.player_hand)
                    game.messages.append(game.player_hand)
                    continue       #Allows the user to start at the top of the loop
                else: 
                    pass #break?? / pass
            
            #2nd Play = Computer's choice and show
            flop = s.next_card(game.running_values, game.running_cards, game.computer_hand[1:])
            if flop != None:           #Normal Play 
                game.comp_rsco, total_sum = analyze(flop, game.comp_rsco)
                #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
                game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                ###CHECK FOR WIN
                if game.computer_score + game.comp_rsco >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                    break
                else:
                    pass
                if total_sum == 31:
                    game.running_values.clear()
                    #print('')
                else:
                    pass
                nflop = game.computer_hand.index(flop)
                game.computer_hand.pop(nflop)
                game.computer_played.append(flop)
            else: #'comp' & 0          #use go procedure ---------------
                if nflop != 0 and got == 'x': #(indicating the player hasn't reciprocated the go)
                    #print('Go! ----->')
                    game.messages.append('Go! ----->')
                    #print(game.player_hand)
                    game.messages.append(game.player_hand)
                    got = 'comp'
                    continue
                elif got == 'comp':
                    game.player_rsco = go(flop, game.player_rsco)
                    #Computer's turn  (maybe put the computer gameplay in that part of the go)
                    seq_value, seq_hand, orderd = s.sequence(game.computer_hand[1:])
                    w = s.first_card_non(seq_hand, seq_value, orderd)
                    xflop = random.choices(game.computer_hand[1:], weights=w)
                    flop = xflop[0]
                    game.comp_rsco, total_sum = analyze(flop, game.comp_rsco)
                    #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
                    game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                    ###CHECK FOR WIN
                    if game.computer_score + game.comp_rsco >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                        break
                    else:
                        pass
                    nflop = game.computer_hand.index(flop)
                    game.computer_hand.pop(nflop)
                    game.computer_played.append(flop)
            #print(a)
            game.messages.append(game.player_hand)
        
        else: 
        #1st Play = Computer's choice
            if len(game.running_cards) == 0:  #total
                seq_value, seq_hand, orderd = s.sequence(game.computer_hand[1:])
                w = s.first_card_non(seq_hand, seq_value, orderd)
                xflop = random.choices(game.computer_hand[1:], weights=w)
                flop = xflop[0]
            else: 
                flop = s.next_card(game.running_values, game.running_cards, game.computer_hand[1:])

            if flop == None and gotc == 'x':    #user's fault and Computer can't play 
                game.comp_rsco = go(nflop, game.comp_rsco)  #Figuiring out ----------------
                pass #continue maybe
            elif flop != None:
                game.comp_rsco, total_sum = analyze(flop, game.comp_rsco)
                #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
                game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                ###CHECK FOR WIN
                if game.computer_score + game.comp_rsco >= 61:
                    #print("Mr. Crib Win's off of pegging: (point total) points")
                    break
                else:
                    pass
                if total_sum == 31:
                    game.running_values.clear()
                    print('')
                else:
                    pass
                nflop = game.computer_hand.index(flop)
                game.computer_hand.pop(nflop)
                game.computer_played.append(flop) 
            else:      #Let the user make a play 
                #Let user go 
                if nflop == 0 and gotc == 'comp':   #computer's fault 
                    #run go
                    game.player_rsco = go(flop, game.player_rsco)
                    continue
                else: 
                    #print('Go! ----->')
                    game.messages.append('Go! ----->')
                    pass

            #2nd Play = User's turn 
            print(game.player_hand)
            #############
            nflop = input("Choose card # 1, 2, or 3: (If applicable type '0' for a Go):") #user enters integer of card (index)
            nflop = user_error(nflop, game)
            if nflop != 0:    #(run as normal)
                flop = game.player_hand[nflop]  #value / card 
                game.player_rsco, total_sum = analyze(flop, game.player_rsco)
                #print(flop + ' --> Total is: ' + str(sum(game.running_values)) + '\n')
                game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                ###CHECK FOR WIN
                if game.player_score + game.player_rsco >= 61:
                    #print("You Win off of pegging: (point total)")
                    break
                else:
                    pass
                if total_sum == 31:
                    game.running_values.clear()
                    #print('')
                else:
                    pass
                game.player_hand.pop(nflop)
                game.player_played.append(flop)
    
            else: 
                if flop != None:
                    #print('Go! ----->')
                    game.messages.append('Go! ----->')
                    gotc = 'x'                   #go is user fault
                    pass  
                elif nflop == 0 and gotc == 'x':
                    #go procedure -------------
                    game.comp_rsco = go(nflop, game.comp_rsco)
                    nflop = input("Choose card # 1, 2, or 3: (If applicable type '0' for a Go):")
                    #---Figure it out with the html input----############
                    nflop = user_error(nflop, game)
                    flop = game.player_hand[nflop]  #value / card 
                    game.player_rsco, total_sum = analyze(flop, game.player_rsco)
                    #print(flop + ' --> Total is: ' + str(sum(game.running_values)))
                    game.messages.append(flop + ' --> Total is: ' + str(sum(game.running_values)))
                    ###CHECK FOR WIN
                    if game.player_score + game.player_rsco >= 61:
                    #print("You Win off of pegging: (point total)")
                        break
                    else:
                        pass
                    game.player_hand.pop(nflop)
                    game.player_played.append(flop)
    
    #print('---Pegging Completed---')
    game.messages.append('---Pegging Completed---')
    #print("Mr. Crib's Points: " + str(game.comp_rsco))
    game.messages.append("Mr. Crib's Points: " + str(game.comp_rsco))
    #print("Your Points: " + str(game.player_rsco))
    game.messages.append("Your Points: " + str(game.player_rsco))
    return game.player_rsco, game.comp_rsco
    
    #Hand Play    

def hand(a_tot, b_tot, top_cd, game): #total from pegging  (4 RETURNS)
    #t.sleep(2)
    #print('\n---Hand Play---')
    game.handages.append('------- Hand Play -------')
    pa_total = a_tot    #remain with pegging value
    pb_total = b_tot    #remain with pegging value 
    game.player_played.append(top_cd)
    game.computer_played.append(top_cd)
    #print('Top Card is: ' + top_cd + '\n')
    game.handages.append('Top Card is: ' + top_cd)
    game.handages.append(' ')
    if game.player_hand[0] == '#':
        #t.sleep(1.5)
        #print('Non-Dealer (Your) Hand Totals:')
        game.handages.append('Non-Dealer (Your) Hand Totals:')
        #count (non-dealer) user's hand first 
        #print(ah)
        game.handages.append(game.player_played.copy())
        a_tot = h.analyze_2(a_tot, game.player_played, game)
        hatot = a_tot - pa_total
        if hatot < 0:
            hatot = 0 
        #print('Your Total is: ' + str(hatot) + '\n')
        if a_tot + game.player_score >= 61:
            game.player_rsco = a_tot
            win(game)
            return game.player_rsco, game.comp_rsco, pa_total, pb_total
        #if win(game) is True:
        #    return game.player_rsco, game.comp_rsco, pa_total, pb_total
        game.handages.append('Your Total is: ' + str(hatot))
        game.handages.append(' ')
        ###count (dealer) computer's hand last 
        #t.sleep(1.25)
        #print("Dealer's (Mr. Crib's) Hand Totals:")
        game.handages.append("Dealer's (Mr. Crib's) Hand Totals:")
        #print(bh)
        game.handages.append(game.computer_played.copy())
        b_tot = h.analyze_2(b_tot, game.computer_played, game)
        hbtot = b_tot - pb_total
        if hbtot < 0:
            hbtot = 0
        #print("Mr. Crib's Total is: " + str(hbtot) + '\n')
        if b_tot + game.computer_score >= 61:
                    game.comp_rsco = b_tot
                    win(game)
                    return game.player_rsco, game.comp_rsco, pa_total, pb_total
        #if win(game) is True:
        #            return
        game.handages.append("Mr. Crib's Total is: " + str(hbtot))
        game.handages.append(" ")
    
    else:
        #count computer (non-d) first
        #t.sleep(1)
        #print("Non-Dealer (Mr. Crib's) Hand Totals:")
        game.handages.append("Non-Dealer (Mr. Crib's) Hand Totals:")
        #print(bh)
        game.handages.append(game.computer_played.copy())
        b_tot = h.analyze_2(b_tot, game.computer_played, game)
        hbtot = b_tot - pb_total
        if hbtot < 0:
            hbtot = 0
        #print("Mr. Crib's Total is: " + str(hbtot) + '\n')
        if b_tot + game.computer_score >= 61:
            game.comp_rsco = b_tot
            win(game)
            return game.player_rsco, game.comp_rsco, pa_total, pb_total
        #if win(game) is True:
        #            return
        game.handages.append("Mr. Crib's Total is: " + str(hbtot))
        game.handages.append(" ")
        ###user = dealer last 
        #t.sleep(1.25)
        #print("Dealer's (Your) Hand Totals:")
        game.handages.append("Dealer's (Your) Hand Totals:")
        #print(ah)
        game.handages.append(game.player_played.copy())
        a_tot = h.analyze_2(a_tot, game.player_played, game)
        hatot = a_tot - pa_total
        if hatot < 0:
            hatot = 0
        #print('Your Total is: ' + str(hatot) + '\n')
        if a_tot + game.player_score >= 61:
                game.player_rsco = a_tot
                win(game)
                return game.player_rsco, game.comp_rsco, pa_total, pb_total
        #if win(game) is True:
        #            return
        game.handages.append('Your Total is: ' + str(hatot))
        game.handages.append(" ")
    game.running_cards.clear()
    game.running_values.clear()
    game.phase = 'TOTALS'
    return a_tot, b_tot, pa_total, pb_total #hatot = Player Hand Score #hbtot = Computer Hand Score 
    
def return_cards(u_hand, ai_hand, topc, deck:list): #RETURN DECK
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

def finish(game): #NO RETURNS
    game.messages.clear()
    game.handages.clear()
    game.player_played.clear()
    game.computer_played.clear()
    game.running_cards.clear()
    game.running_values.clear()

    game.player_rsco = 0
    game.comp_rsco = 0
    game.pp_score = 0   
    game.cp_score = 0 

    game.begin = "NO"
    game.go = "None"

    game.phase = "DEAL"
    game.messages.append('*#*#*#*Round ' +  str(game.round) + '*#*#*#*')
    
if __name__ == '__main__':
    main()    

