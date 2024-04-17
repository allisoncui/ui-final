from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

# ROUTES

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/intro')
def intro():
    return render_template('intro.html')
@app.route('/strategies')
def strategies():
    # Logic to render strategies page
    return render_template('strategies.html')

@app.route('/quiz')
def quiz():
    # Logic to render quiz page
    return render_template('quiz.html')
if __name__ == '__main__':
    app.run(debug=True)
