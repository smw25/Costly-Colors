# Costly Colours

## Description
Costly Colours, sometimes just called Costly, is a historical English card game for two players and a "fascinating relative of cribbage". The game "requires a moderate amount of skill in playing, and is well adapted to teach quickness in counting". It has more combinations than cribbage and retains the original scoring system for points, but does not use a 'crib'. In the 19th century it was described as "peculiar to Shropshire" (Wikepedia). Due to the realtively niche nature of this ancient game, this program attempts to create an online versions where a user can compete against a computer (with relative strategy) using the scoring rules of Costly Colours. 

## Visuals
The game is shown by printing a title line and the user's card hand (contained in list brackets) as well as the top card. New lines will print the situations occur during pegging gameplay and the computer will automatically calculate hand scores (in the correct order, per dealer) during hand scoring. Each combination for points appears with '+ However many points' the computer or the player recieves. The computer is named "Mr. Crib" as a nod to the decendent of this game in cribbage proper. 

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.
'#' = This symbol indicates that on this round you are the non-dealer. You will lay down the first card during pegging, and you will count all points available in your hand first during the hand-counting phase.
'*D' = This symbol indicates that you are the dealer during this round. If a Jack or Deuce (2) is the turn up card for the round you will automatically peg 4 for "His Heels" if a Jack or 4 for the Deuce. 

## Roadmap
1. COMPLETE - Game stoppage in the middle of pegging. This will more than likely occur the need of passing the cumulative totals of bot the computer and the user into the pegging() function as new imputs and returning an output in case a break occurs and a "player" wins off of pegging. I forsee much troubleshooting occuring with this in the future
2. "Mogging" Feature: According to sources with the rules of this anceint game: 
    '*After the deal and turn-up, the players may now "mog". This is done by each passing a card from his hand face down to the other. If either refuses to mog, the other pegs one hole for the refusal. If either gives away Jack or a Deuce, he may first peg 2, or 4 if it is the "right" Jack or Deuce (of the same suit as the turn-up). If he neglects to do so, the other may peg for it when the hands are finally counted (but not before).*' 
    This could be accomplished by creating a function before pegging and after initial which asks the computer or player if they want to swap a card. The .pop() and .append() will become useful in this case for taking out and replacing the card. Finding strategy for the computer with mogging could be difficult 
3. COMPLETE - Taking out sequences from the first_card() decision making in the computer since runs do not count during hand play in this game. 

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
