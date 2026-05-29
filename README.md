# Costly Colours

## Description
Costly Colours, sometimes just called Costly, is a historical English card game for two players and a "fascinating relative of cribbage". The game "requires a moderate amount of skill in playing, and is well adapted to teach quickness in counting". It has more combinations than cribbage and retains the original scoring system for points, but does not use a 'crib'. In the 19th century it was described as "peculiar to Shropshire" (Wikepedia). Due to the realtively niche nature of this ancient game, this program attempts to create an online versions where a user can compete against a computer (with relative strategy) using the scoring rules of Costly Colours. 

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
when given 0 retrieving *D* or # this should indicate a go
    if go is called then all "totals" lists should be emptied 

this could be solved by making another if loop in the initial 'if' for who is dealer
    this if would right after nflop 
    if nflop != 0, then run as normal
    if nflop == 0 then we run Go procedures 

doing this for the computer strats would include: 
    making a larger if-else at the start of the addition section 
    if would be if current 