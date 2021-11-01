
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "lets guess a number"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,101)
        print(session['num'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print(session['guess'])
    redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)