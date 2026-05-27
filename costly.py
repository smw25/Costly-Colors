import random

suits = ["Diamonds", "Hearts", "Clubs", "Spades", ]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

a = [] #user's hand
b = [] #computer's hand 

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

#Pegging play
def play(top:str):
    a_points = int(0)
    b_points = int(0)
    #if top card is Jack or Deuce add 4 points to dealer of 'His Heels'
    top_type = top[0:4]
    if top_type == 'Jack':
        if a[0] == '*D*':
            a_points += 4
        else:
            b_points += 4
        print('His Heels +4')
    if top_type == '2 of':
        if a[0] == '*D*':
            a_points += 4
        else:
            b_points += 4
        print('Duece Down +4')
    return a_points, b_points
    
    #Pegging Play
    #Non-dealer starts
    #if a[0] == '*D*':
        #flop = int(input("Choose card # 1, 2, or 3: ")) #user enters integer of card
    #else: 
        #random.choices(b[1:3], weights=[])
        #xflop = b[0]
        

def main(): 
    main_deck = cards()
    main_deck = start(main_deck)
    trump = deal(main_deck)
    a_point, b_point = play(trump)


if __name__ == '__main__':
    main()    

