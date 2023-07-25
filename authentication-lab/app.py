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
  "https://example-fierbase-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the input values from the form
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            full_name = request.form['full_name']
            username = request.form['username']
            bio = request.form['bio'][:280]  # Truncate to a maximum of 280 characters

            # Create a dictionary with user information
            user = {
                'full_name': full_name,
                'username': username,
                'bio': bio
            }

            # Add the user to the database using their uid (retrieve it through login_session)
            uid = login_session['user']['localId']  # Replace with the actual way of retrieving the uid
            db.child('Users').child(uid).set(user)
            return redirect(url_for('signin'))
       except:
           error = "Authentication failed"
       

        # Redirect to a success page or do something else
        return redirect('/success')  # Replace '/success' with the desired success page

    return render_template('signup.html')

# Route for the add_tweet page
@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        # Get the input values from the form
        title = request.form['title']
        text = request.form['text'][:280]  # Truncate to a maximum of 280 characters

        # Create a dictionary with tweet information
        tweet = {
            'title': title,
            'text': text,
            'uid': login_session['user']['localId']   # Replace with the actual way of retrieving the uid
        }

        # Add the tweet to the database with a random key
        db.child('Tweets').push(tweet)

        # Redirect to a success page or do something else
        return redirect('/success')  # Replace '/success' with the desired success page

    return render_template('add_tweet.html')

# Route for displaying all tweets
@app.route('/all_tweets')
def all_tweets():
    # Get all the tweets from the database
    tweets = db.child('Tweets').get()

    return render_template('tweets.html', tweets=tweets)



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


if __name__ == '__main__':
    app.run(debug=True)