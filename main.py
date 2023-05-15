from flask import Flask, render_template, request, redirect, url_for, session

from hashlib import sha256

app = Flask(__name__)
app.secret_key = '7e8dfb5aa7809c4efc7c5edc95a67f42'

# User data placeholder (replace with a proper database)
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = sha256(password.encode('utf8')).hexdigest()
        # Save the hashed password to the database or data placeholder
        users.append({'username': username, 'password': hashed_password})

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = sha256(password.encode('utf8')).hexdigest()

        # Check if the user exists in the database or data placeholder
        for user in users:
            if user['username'] == username and user['password'] == hashed_password:
                session['username'] = username  # Store the username in the session
                return redirect(url_for('connect'))

        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        # Perform necessary actions to establish the connection with the robot
        
        # Redirect to the page with the streamed YouTube video
        return redirect('/streaming')
    else:
        username = session.get('username')  # Retrieve the username from the session
        return render_template('dashboard.html', username=username)

@app.route('/streaming')
def video():
    return render_template('streaming.html')

if __name__ == '__main__':
    app.run()
