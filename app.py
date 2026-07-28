###ALL VIBED FROM GOOGLE###
from flask import Flask, render_template, request
from state import GameState
import xgameplay as g
import xcostly as c
app = Flask(__name__)

usertot = 0
comptot = 0 
game = GameState()
    
# Route for the home page   ----may not be necessary-----
@app.route('/', methods=['GET', 'POST'])
def home():
    # Send variables directly to index.html
    ###
    name = ''
    start = request.form.get('start')
    if start == "TRUE" and game.phase == "NOT":
        game.begin = "IN"
        name = '*#*#*#*#*Costly Colours*#*#*#*#*'
        c.cards(game)       #onload="document.getElementById('start.reset();')"
        c.start(game) 
        game.phase = "DEAL"

    if game.phase != "NOT":
        name = '*#*#*#*#*Costly Colours*#*#*#*#*'

    if game.phase == "DEAL":
        c.deal(game)
        c.initial(game)
        game.phase = "MOG?"
        ##Check Win

    if game.phase == "MOG?" and request.form.get('mogg') is not None:
        mogg = request.form.get('mogg')
        trade = request.form.get('card')
        c.mog_choice(game, mogg)
        #if mogg == 'Y' or mogg == 'Y':
        #card_choice = computers card 
        game.phase = "MOGGING"

    #card_choice = something means computer is a Y, and if form 'card' = something player is Y
    if game.phase == "MOGGING" and game.card_choice and request.form.get('card') is not None:
        trade = request.form.get('card')
        c.mogging(game, trade, game.card_choice)
        game.phase = "PEG1"

    
    return render_template('index.html', c_title=name, start=start, 
                           messages=game.messages,
                           game=game 
                           )
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True auto-reloads the browser when you change code
