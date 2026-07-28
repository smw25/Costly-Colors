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
    if start == "TRUE":
        game.begin = "IN"
        name = '*#*#*#*#*Costly Colours*#*#*#*#*'
        c.cards(game)       #onload="document.getElementById('start.reset();')"
        c.start(game)
    if game.begin == "IN":
        top_card = c.deal(game)
        p_round_pnts, comp_round_pnts = c.initial(game, top_card)
        ##C
        mogg = request.form.get('mogg')
        trade = request.form.get('card')
        p_round_pnts, comp_round_pnts = c.mogging(p_round_pnts, comp_round_pnts, top_card, game, mogg, trade)
    return render_template('index.html', c_title=name, start=start, messages=game.messages,game=game
        )
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True auto-reloads the browser when you change code
