###ALL VIBED FROM GOOGLE###
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    # Define backend Python data
    user_name = "Player"
    programming_languages = ["Python", "HTML", "CSS", "JavaScript"]
    
    # Send variables directly to index.html
    return render_template('index.html', name=user_name, languages=programming_languages)

# Route to handle form data sent from the HTML website
@app.route('/submit', methods=['POST'])
def submit():
    # Catch the data typed into the HTML form
    user_input = request.form.get('user_message')
    return f"<h1>Backend Received Your Message: {user_input}</h1>"

if __name__ == '__main__':
    app.run(debug=True)  # debug=True auto-reloads the browser when you change code
