from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
HARD_ATTEMPTS = 3

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    win = False
    lose = False
    attempts_left = session.get('attempts')  # get attempts from session if exists

    if request.method == 'POST':
        if 'level' in request.form:
            level = request.form['level']
            session['number'] = random.randint(1, 100)
            session['attempts'] = EASY_ATTEMPTS if level == 'Easy' else HARD_ATTEMPTS
            session['level'] = level
            attempts_left = session['attempts']
            message = f"You chose {level} level. Start guessing!"
        elif 'guess' in request.form:
            guess = int(request.form['guess'])
            number = session.get('number')
            session['attempts'] -= 1
            attempts_left = session['attempts']

            if guess < number:
                message = "Too low!"
            elif guess > number:
                message = "Too high!"
            else:
                message = f"Correct! The number was {number}."
                win = True
                clear_session()
                attempts_left = None  

            if attempts_left == 0 and not win:
                message = f"You've run out of attempts! The number was {number}."
                lose = True
                clear_session()
                attempts_left = None 

    return render_template('index.html', message=message, win=win, lose=lose, attempts_left=attempts_left)

def clear_session():
    session.pop('number', None)
    session.pop('attempts', None)
    session.pop('level', None)

if __name__ == '__main__':
    app.run(debug=True)
