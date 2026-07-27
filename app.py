###ALL VIBED FROM GOOGLE###
from flask import Flask, render_template, request
import xgameplay as g
app = Flask(__name__)

usertot = 0
comptot = 0 
    
# Route for the home page   ----may not be necessary-----
@app.route('/', methods=['GET', 'POST'])
def home():
    # Define backend Python data
    name, card_deck = g.begin()
    # Send variables directly to index.html
    return render_template('index.html', c_title=name)

#@app.route('/', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True auto-reloads the browser when you change code
