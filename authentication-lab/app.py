from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
config = {
  "apiKey": "AIzaSyCeBzjV9TxITxZS4wQeujO_K7my5bRnF7U",
  "authDomain": "example-fierbase.firebaseapp.com",
  "projectId": "example-fierbase",
  "storageBucket": "example-fierbase.appspot.com",
  "messagingSenderId": "912395945293",
  "appId": "1:912395945293:web:374ec378b3772a467ee304",
  "measurementId": "G-9PFDQY6EXY",
  "databaseURL": ""
}



@app.route('/', methods=['GET', 'POST'])
def signup():
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('signin'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('/add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)