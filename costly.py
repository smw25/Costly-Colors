import random

suits = ["Diamonds", "Hearts", "Clubs", "Spades", ]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

a = [] #user's hand
b = [] #computer's hand 
total = []
ntotal = []

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
    return top

def analyze(c_card:str, player_total):
    vitals = c_card.split(' ') #list with ['#', 'of', 'suit']
    #add to running total pile
    total.append(vitals[0])  #string value stays in total 
    #analyze running total function
  #pairs first 
    if total[-4] == total[-3] == total[-2] == total[-1]:
        player_total += 18
        print('Double Prial (4-of-a-kind) +18')
    elif total[-3] == total[-2] == total[-1]:
        player_total += 9 
        print('Prial (3-of-a-king) +9')
    elif total[-2] == total[-1]:
        player_total += 2
        print('Pair +2')

  #sequence second 
    ordtotal = sorted(total, key=ranks.index) #sorted total sequence strings 
    if len(ordtotal) >= 3:
        if ordtotal in ranks:
            player_total += len(ordtotal)
            numadd = str(len(ordtotal))
            print('Sequence +' + numadd)
        else: 
            pass
    else: 
        pass        
    #change face cards to numbers of summation points 
    if vitals[0] == 'Jack' or vitals[0] == "Queen" or vitals[0] == "King" :
        vitals[0] = 10
    elif vitals[0] == 'Ace':
        vitals[0] = 1
    else:
        vitals[0] = int(vitals[0])

  #sums third 
    if sum(total) == 31:
        numadd = len(total)
        player_total += numadd
        print('31 +' + numadd)
    elif sum(total) == 25:
        numadd = len(total)
        player_total += numadd
        print('25 +' + numadd)
    elif sum(total) == 15:
        numadd = len(total)
        player_total += numadd
        print('15 +' + numadd)
    return player_total
    
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
    
#Pegging Play
def pegging(a_tot, b_tot):
    #Non-dealer starts
    #could put this in a 'for' loop x in range(6)
    if a[0] == '#':
        nflop = int(input("Choose card # 1, 2, or 3: ")) #user enters integer of card
        flop = a[nflop]
        a_tot = analyze(flop, a_tot)
        print(flop + ' --> Total is: ' + total)
        print('Your Total: ' + a_tot)
        #run computer's choice and show 
    else: 
        #random.choices(b[1:3], weights=[])
        flop = b[1]

    #Hand Play
    #     
    
    
def main(): 
    main_deck = cards()
    main_deck = start(main_deck)
    trump = deal(main_deck)
    a_point, b_point = initial(trump)
    #pegging(a_point, b_point)

if __name__ == '__main__':
    main()    

