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
        ##Check 
        
    if game.phase == "MOG?" and request.form.get('mogg') is None:
            c.mog_choice(game, None)
            return render_template('index.html', c_title=name, start=start, messages=game.messages, game=game)
    if game.phase == "MOG?" and request.form.get('mogg') is not None:
        mogg = request.form.get('mogg')
        trade = request.form.get('card')
        c.mog_choice(game, mogg)
        #card_choice = computers card 
        #game.phase = "MOGGING"
    
    #card_choice = something, means computer is a Y, and if form 'card' = something player is Y
    if game.phase == "MOGGING" and game.card_choice and request.form.get('card') is not None:
        trade = request.form.get('card')
        t = c.user_error(trade, game)
        if t is False:
            return render_template('index.html', c_title=name, start=start, messages=game.messages, game=game)
        c.mogging(game, trade, game.card_choice)
        #game.phase = "PEG_START"
        if game.player_hand[0] == '#':   #Player is a non-dealer
            return render_template('index.html', c_title=name, start=start, messages=game.messages, game=game)
        else:
            pass
    
    if game.phase == "PEG_START":
        c.start_peg(game)
        
    p_choice = request.form.get('card') 

    if game.phase == 'PLAYER_TURN' and request.form.get('card') is not None:
        t = c.user_error(p_choice, game)
        if t is False:
            return render_template('index.html', c_title=name, start=start, messages=game.messages, game=game)
        p_choice = int(p_choice)
        c.player_peg(game, p_choice) 
    if game.phase == 'COMP_TURN':
        c.comp_peg(game)
    if game.phase == 'END_PEG':
        c.peg_stop(game)

    return render_template('index.html', c_title=name, start=start, 
                           messages=game.messages,
                           game=game 
                           )
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True auto-reloads the browser when you change code
