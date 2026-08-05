###INITIAL LAYOUT VIBED FROM GOOGLE###
from flask import Flask, render_template, request, session
import uuid
from state import GameState
import xhand as h
import xcostly as c
app = Flask(__name__)

#game = GameState()
games = {}

app.secret_key = 'combinations_n0t_permutations_c140c'

def get_game():
    #if a new person goes to the website, they won't have game_id in their session
    if "game_id" not in session:
        session["game_id"] = str(uuid.uuid4()) 
        #session is a dictionary so the "game_id" is the content/key and the str(of session name) is data/entry 

    gid = session["game_id"]

    if gid not in games:
        games[gid] = GameState()

    return games[gid]
    
# Route for the home page   ----may not be necessary-----
@app.route('/', methods=['GET', 'POST'])
def home():
    #global game
    game = get_game()
    # Send variables directly to index.html
    ### ----- 
    round = request.form.get('next')
    reset = request.form.get('reset')
    if game.phase == 'FINISH' and round is not None:
        game.round += 1
        c.finish(game)
    elif game.phase == 'GAME_OVER' and reset is not None:
        #game = GameState()
        #game.reset()
        games[session["game_id"]] = GameState()
        game = games[session["game_id"]]
    elif reset is not None:
        #game = GameState()
        #game.reset()
        games[session["game_id"]] = GameState()
        game = games[session["game_id"]]

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
        ###TOP Splitting -----------------
        game.top_split = game.top.split()
        game.top_split[-1] = game.top_split[-1].lower()
        if game.phase == "GAME_OVER":
            pass
        else:
            game.phase = "MOG?"
        ##Check 
        
    if game.phase == "MOG?" and request.form.get('mogg') is None:
            c.mog_choice(game, None)
            #return render_template('index.html', c_title=name, start=start, messages=game.messages, game=game)
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

    if game.phase == 'HANDS' and request.form.get('move-on') is not None:
        game.messages.clear()
        game.player_rsco, game.comp_rsco, game.pp_score, game.cp_score = c.hand(game.player_rsco, game.comp_rsco, game.top, game)

    if game.phase == 'TOTALS':
        h.round_totals(game.player_rsco, game.comp_rsco, game.pp_score, game.cp_score, game)
        h.grand_totals(game) #phase = 'FINISH'

    if game.phase == 'GAME_OVER':
        #need to add something to reset everything 
        pass
    return render_template('index.html', c_title=name, start=start, 
                           messages=game.messages,
                           game=game 
                           )
    
@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/scoring')
def scoring_eg():
    return render_template('scoring.html')

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)  # debug=True auto-reloads the browser when you change code
