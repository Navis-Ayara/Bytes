from flask import Flask,render_template,request,redirect,url_for,sessions,session
from database import get_database
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.run['SECRET_KEY'] = os.urandom(24)

def get_current_user():
    user = None
    if 'user' in session:
        user = session['user']
        db = get_database()
        user_cusor = db.execute("select * from users where username = ?", [user])
        user = user_cusor.fetchone()
    return user



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home():
    user = get_current_user()
    return render_template('home.html', user=user)

@app.route('/login',methods=['GET', 'POST'])
def login():
    user = get_current_user()
    error = None
    if request.method == 'POST':
        # get form data
        username = request.form['username']
        user_enter_password = request.form['password']
        db = get_database()
        cursor = db.execute('SELECT * FROM users WHERE username = ?', [username])
        user = cursor.fetchone()
        
        if user:
            if check_password_hash(user['password'], user_enter_password):
                session['user'] = user['username']
                return redirect(url_for('home'))
            else:
                error = 'Invalid username or password'
    return render_template('login.html', loginerror=error, user=user)
       


@app.route('/register',methods=['GET', 'POST'])
def register():
    user = get_current_user()
    register_error = None
    if request.method == 'POST':
        # get form data
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        db = get_database()
        #duplicate check    
        user_cusor = db.execute("select * from users where username = ?", [username])
        existing_user = user_cusor.fetchone()

        if existing_user:
            register_error = 'Username already exists'
            return render_template('register.html', register_error=register_error)

        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, password],'0')
        db.commit()
        return redirect(url_for('login'))

    return render_template('register.html', register_error=register_error, user=user)


@app.route('/logout')
def logout():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
