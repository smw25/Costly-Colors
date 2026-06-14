import costly as c
import hand as h 
import random as r
import time 

main_deck = c.cards()
main_deck = c.start(main_deck)
print('*#*#*#*#*Costly Colours*#*#*#*#*')

def gameplay():
    usertot = 0
    comptot = 0 
    while usertot < 121 or comptot < 121:
        trump = c.deal(main_deck)
        a_point, b_point = c.initial(trump)
        #ma_point, mb_point = c.mogging()
        pa_point, pb_point = c.pegging(a_point, b_point, usertot, comptot)  #just the initial totals for the round
        #add pegging points to player totals and if they exceed 121 were done 
        if c.a[0] == '#':  #Human is non-dealer
            if usertot + pa_point >= 61:
                usertot += pa_point 
                break
            elif comptot + pb_point >= 61:
                comptot += pb_point
                break
            else:
                pass
        else:   #Computer is non-dealer
            if comptot + pb_point >= 61:
                comptot += pb_point
                break
            elif usertot + pa_point >= 61:
                usertot += pa_point
                break
            else:
                pass
        a_point, b_point = c.hand(pa_point, pb_point, trump)
        h.round_totals(a_point, b_point, pa_point, pb_point) #just displays totals
        usertot += a_point  
        comptot += b_point
        if c.a[0] == '#':  #Human is non-dealer
            if usertot >= 61:
                break
            elif comptot >= 61:
                break
            else:
                pass
        elif c.b[0] == '#':
            if comptot >= 61:
                break
            elif usertot >= 61:
                break
            else:
                pass
        time.sleep(1.5)
        print('\n*#*#*Grand Totals*#*#*')
        print('Mr. Crib = ' + str(comptot))
        print("Your's = " + str(usertot))
        card_deck = c.return_cards(c.ah, c.bh, trump, main_deck)
        if c.a[0] == '*D*': #if user was dealer
            c.a[0] = '#'    #user is now pone
        else:
            c.a[0] = '*D*'  #user was pone and now dealer
        
        if c.b[0] == '*D*': #if computer was dealer
            c.b[0] = '#'    #computer is now pone
        else:
            c.b[0] = '*D*'  #if computer was pone now dealer
        r.shuffle(card_deck)
        r.shuffle(card_deck)
        r.shuffle(card_deck)
        print('\n *#*#*#*Next Round*#*#*#*')

    #Winner Declaration         (add avg pegging and hand scores???)
    if c.a[0] == '#':
        if usertot >= 61:
            time.sleep(1.5)
            print('\n*#*#*Grand Totals*#*#*')
            print('Mr. Crib = ' + str(comptot))
            print("Your's = " + str(usertot))
            print('*#*#*#*#*You win with a total of: ' + str(usertot) + '*#*#*#*#*')
        elif comptot >= 61:
            time.sleep(1.5)
            print('\n*#*#*Grand Totals*#*#*')
            print('Mr. Crib = ' + str(comptot))
            print("Your's = " + str(usertot))
            print('*#*#*#*#*Mr. Crib wins with a total of: ' + str(comptot) + '*#*#*#*#*')
    elif c.b[0] == '#':
        if comptot >= 61:
            time.sleep(1.5)
            print('\n*#*#*Grand Totals*#*#*')
            print('Mr. Crib = ' + str(comptot))
            print("Your's = " + str(usertot))
            print('*#*#*#*#*Mr. Crib wins with a total of: ' + str(comptot) + '*#*#*#*#*')
        elif usertot >= 61:
            time.sleep(1.5)
            print('\n*#*#*Grand Totals*#*#*')
            print('Mr. Crib = ' + str(comptot))
            print("Your's = " + str(usertot))
            print('*#*#*#*#*You win with a total of: ' + str(usertot) + '*#*#*#*#*')

gameplay()
    
