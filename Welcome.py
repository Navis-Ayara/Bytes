from Flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/Welcome')
def Welcome():
    return f"Welcome to our blog its under development"

if __name__ == '__main__':
    app.run(debug=True)
    
