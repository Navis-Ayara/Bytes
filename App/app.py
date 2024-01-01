from flask import Flask, render_template, request, redirect, url_for
import pymongo
from user import routes
app = Flask(__name__)

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system



@app.route('/')
def home():
    return redirect(url_for('Welcome'))

@app.route('/Welcome')
def Welcome():
    return render_template("Welcome.html")

@app.route('/login')
def login():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
    
