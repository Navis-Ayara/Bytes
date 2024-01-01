from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('Welcome'))

@app.route('/Welcome')
def Welcome():
    return render_template("Welcome.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
    
