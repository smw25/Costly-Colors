# Costly Colours

## Description
Costly Colours, sometimes just called Costly, is a historical English card game for two players and a "fascinating relative of cribbage". The game "requires a moderate amount of skill in playing, and is well adapted to teach quickness in counting". It has more combinations than cribbage and retains the original scoring system for points, but does not use a 'crib'. In the 19th century it was described as "peculiar to Shropshire" (Wikepedia). Due to the realtively niche nature of this ancient game, this program attempts to create an online versions where a user can compete against a computer (with relative strategy) using the scoring rules of Costly Colours. 

## Original Game Instructions ("The Complete Gamester" - Charles Cotton)
This game is to be play'd out only by two persons, of which the eldest is to play first as in other games. You must deal off three a piece, and turn up the next Card following; then the Eldest is to take his choice whether he will Mogg, (that is change a Card or no) and whosoever refuseth is to give the other one chalk or hole [point], of which generally Threescore and one [61] makes the Game. Then must the Eldest play, and the other if he can must make it up fifteen, for which she shall set up as many holes or chalks as there are cards upon the Table; so likesie for five and twenty [25], and also as many Cards as are play'd to make up thiry, no more nor less, so many chalks may be set up who play'd last, to make up one and thurty, and if one and thirty be not made, then he that play'd last and is nearest one and thirty without making out must set up one, which is called setting up one for the latter. 

This being done, the eldest must show how many Chalks he hath in his hand to set up, and after him the youngest, which they must reckon in this manner, taking notice both of the colour and number of pips upon the Card turn'd up as those in thier hands still reckoning as many for all the fifteen and five and twenty as there go Cards to make the number; and if you have it by chance in your hand, and with the Card turned up one and thiryt, then you must se tup four for that: you must also set up if you have them in your hands or can make them so in the Card turn'd up as followeth; two for a pair, be they either Coat-cards [Face cards] or others; two for a Knave [Jack], and if a Knave of the same colour and suit of the Card turn'd up, then you must set up four; and so for a Deuce four, if it be of the same colour turn'd up: if you have three of a sort [Trips], either three fours, five, five, sixes or Coat-cards, you must set up nine, and this is called a Pair-Royal; now if thye are all either Hearts, Diamonds or the like then you must set up six for *Costly-Colours*. If you have three of a colour you can reckon but two for Colours. 

Whosoever dealt, if he turn'd up eithe rDeuce or Knave, he must se tup four for it; as for example, imagine you had dealt your Adversary three cards, *viz.* the five of Hearts, four of Hearts, and eight of Hearts; to your self the Deuce of Hearts, seven of Clubs, and nine of Hearts. Lastly, you turn up a Card, which is the Knave of Hearts, for which you must set up four; then because he will not ask you to change one, he gives you one, which you must set up, and then he plays, suppose it be his five of Hearts, you then play your seven of Clubs, which makes twleve, then he plays his eight of Hearts, which makes twentyl then you player your nine of Hearts, which makes twenty nine, and because he cannot come in with his five of Hearts, you must play your Deuce of Hearts, which makes you one and thirty. For your five you must set up five, then he must set up what he hath in his hand, which you will find to be but six, for he hath nothing in his hand but *Costly-Colours*. Then must you set up your Games, which first are two, for your nine of Clubs and nine of Hearts which make fifteen, then that fifteen and the Knave turn'd up makes five and twenty, for which set up three; then for your Deuce of Hearts which is the right set up four, and three for Colours, because you have three of a sort in your hand with that turn'd up, now these with the five you got in playing for thirty one makes you this Deal wiht the Knave turn'd up and the Cards in your hand just twenty. Many other examples I might give you, but that is needless since this one is sufficient to direct you in all others. And thus much for *Costly-Colours*. 

## Visuals
The game is shown by printing a title line and the user's card hand (contained in list brackets) as well as the top card. New lines will print the situations occur during pegging gameplay and the computer will automatically calculate hand scores (in the correct order, per dealer) during hand scoring. Each combination for points appears with '+ However many points' the computer or the player recieves. The computer is named "Mr. Crib" as a nod to the decendent of this game in cribbage proper. 

## Usage
### Deal 
At the start of a game you will be dealt a hand comprising of a symbol and 3 strings detailing what cards of a standard 52 card deck you have been dealt. The top card will also be displayed. 
'#' = This symbol indicates that on this round you are the non-dealer. You will lay down the first card during pegging, and you will count all points available in your hand first during the hand-counting phase.
'*D' = This symbol indicates that you are the dealer during this round. If a Jack or Deuce (2) is the turn up card for the round you will automatically peg 4 for "His Heels" if a Jack or 4 for the Deuce. 

### Mogging
Your first decision and source of input will be with the choice of mogging as described in the **Description** section:
```
Would you like to "Mog" (trade a card with Mr. Crib). Type Y or N:
```
After this prompt you only need to type `Y` for yes, or `N` for no in the terminal. Following the decision, 3 outcomes can occur, either:
 
1. If you type `N`, Mr. Crib will recieve +1 point because you refuse to mog
2. If yout type `Y` and Mr. Crib refuses, you recieve +1 point
3. You both choose to mogg and a trade occurs 

### Pegging
Once the mogging stage has been completed the pegging round can begin. Your hand will be re-displayed as strings in the terminal (with your new card if a mogging exchange occured) and you will be given a prompt for input. 
```
Choose card # 1, 2, or 3: (If applicable type '0' for a Go):
```

To choose a card type the number appropriate for slot of the card. For example, if the 'Jack of Hearts' is the second card in your given hand, and you want to play it type `2`. Make sure you pay attention to the order of your cards if mogging occurs, your cards probably moved up a slot. After you play a card, the card is removed from your hand; thereby all cards behind this card are moved up in order (e.g. if you play the second card in your hand at the start of the hand, the #3 card will move up to the 2 slot on your next chance to play during pegging.) After you choose a card to lay down, your card and the culmulative total for the pegging play will be displayed: 
```
Jack of Diamonds --> Total is: 13
```
If any points are gained via pairs, sums, or runs, they will be displayed as well. Then the turn will alternate to Mr. Crib; this back and forth will reoccur until someone pegs 31 or a 'Go' occurs. 

If you cannot play a card without exceeding 31, you must type `0` for the go. Mr. Crib will continue to play a card if he without exceeding 31, wherein you will have to type `0` again. If Mr. Crib can also not play a card but you said 'Go' first Mr. Crib will peg +1 for the 'Go':
```
Go! ----->
Go! +1 for Mr. Crib 
```
This same pattern will occur in reverse, if Mr. Crib declares a go and you can play cards you will have the opportunity to do so. If you can play and which try to type 0 to save your cards you will see a Renege error:
```
**Renege** - You can still play a card (Ace of Diamonds) with Total remaining under 31
Choose the correct card 1 or 2: 
```
If you cannot play without goihg over 31 or have no cards in your hand, input 0 and you will recieve +1 for the Go from Mr. Crib. 
If you input a number that is not one of the card slot positions available (e.g. you type 3, but only have 2 cards in your hand) you will recieve an error:
```
**Out of Position** -- Choose the correct card position 
```

### Hand Counting
Once you and Mr. Crib do not have any more cards in your hands then the game moves on to Hand counting. During this phase the program will calculate all the possible point combinations you can recieve from summations (15, 25, & 31), pairs and prials, and colours. Each hand will be displayed--with the top card added--and combinations for points will be displayed with the non-dealer counting first followed by the dealer.  
```
Non-Dealer (Mr. Crib's) Hand Totals:
['2 of Hearts', '4 of Clubs', '7 of Clubs', '4 of Diamonds']
Jack or Duece in Hand: +2 

Pair of 4s: +2 

(4, 7, 4)
Sum to 15: +3 

Mr. Crib's Total is: 7
```
Totals for the round, delineated by pegging and hand scores are calculated and displayed after this hand counting, then grand totals for total points between Mr. Crib and the user are displayed after. One must score 61 points to win. (Currently you cannot win off of mogging, but you can win based upon)
## Roadmap

1. Statistical Analysis: The ability to track average pegging scores, average hand scares, highest pegging and hand scares, and best possible hand combination before pegging for the user and the computer across all rounds of the game. This will be implemented by saving the points earned during pegging and each round into a readable file format (.csv) which can be ran into R. 
    - Save pegging, hand, and total scores for each round as a row in a csv file (after each run through the gameplay while loop) 
    - In R, read the .csv file, and save contents into a data.frame variable object
    - Run mean(), max(), combinations of 5 card theoretical hand (3 cards dealt + top card + mogged card), and plots to the data added into the data.frame
    - export these values (and plots) back into a .csv file or other comparable file format
    - Display values in either python or R
2. Mogging features to add for computer analysis: 
(a) User has a point total >= 58
(b) Don't Trade 2, 5, or Jack unless total would go up without it (and maybe not even for that)
(c) Work in more strategy into the mogging decision in general. 

3. Make the code path for breaking the loop for wins a function which returns true if player gets past 61, the function should return the player total, and a boolean T or F. This will allow for a smaller code blocks and simple 'if True, then break' statements. 

4. **COMPLETE** - Game stoppage in the middle of pegging. This will more than likely occur the need of passing the cumulative totals of bot the computer and the user into the pegging() function as new imputs and returning an output in case a break occurs and a "player" wins off of pegging. I forsee much troubleshooting occuring with this in the future

5. **COMPLETE** - "Mogging" Feature: According to sources with the rules of this anceint game: 
    '*After the deal and turn-up, the players may now "mog". This is done by each passing a card from his hand face down to the other. If either refuses to mog, the other pegs one hole for the refusal. If either gives away Jack or a Deuce, he may first peg 2, or 4 if it is the "right" Jack or Deuce (of the same suit as the turn-up). If he neglects to do so, the other may peg for it when the hands are finally counted (but not before).*' 
    This could be accomplished by creating a function before pegging and after initial which asks the computer or player if they want to swap a card. The .pop() and .append() will become useful in this case for taking out and replacing the card. Finding strategy for the computer with mogging could be difficult 
6. **COMPLETE** - Taking out sequences from the first_card() decision making in the computer since runs do not count during hand play in this game. 

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Shenard Williams - Duke University: Civil Engineering (Class of 2029)

## License
For open source projects, say how it is licensed.

## Project status
