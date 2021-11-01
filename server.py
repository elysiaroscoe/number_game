
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "lets guess a number"

@app.route('/')
def index():
    if 'guess' in session:
        print('yes')
    else:
        print('no')
    return render_template("index.html")

# @app.route('/calculate')
# def isitequal():
    # if session['guess'] < session['random']:

    # elif session['guess'] > session['random']:
        
    # else

    redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)