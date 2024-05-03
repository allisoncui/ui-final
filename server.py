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
@app.route('/opening_strategy')
def opening_strategy():
    return render_template('opening.html')

@app.route('/strategies')
def strategies():
    # Logic to render strategies page
    return render_template('strategies.html')
@app.route('/imperfection')
def imperfection_strategy():
    return render_template('imperfection.html')
@app.route('/king_cash')
def king_cash():
    return render_template('king_cash.html')
@app.route('/genuinity')
def genuinity():
    return render_template('genuinity.html')
@app.route('/avoid')
def avoid():
    return render_template('avoid.html')
@app.route('/quiz')
def quiz():
    # Render quiz page with question data
    question_data = {
        'question': 'You are given a vase that has a slight crack on the side. It costs $50 because it belongs to an antique collection. What would be your first comment to bargain the price?',
        'choices': [
            'I don’t care too much about antique vases. Could you lower the price to $30?',
            'There is a crack on the side of the vase, meaning it’s been used. Could you lower the price to $40?',
            'I’ll pay the full amount in cash if it is lowered to $30.',
            'Your nextdoor neighbor is selling a very similar vase for just $25.'
        ],
        'correct_answer': 'There is a crack on the side of the vase, meaning it’s been used. Could you lower the price to $40?'
    }
    return render_template('quiz.html', question_data=question_data)

@app.route('/quiz/result', methods=['POST'])
def quiz_result():
    # Logic to handle quiz submission and result
    selected_choice = request.form['choice']
    correct_answer = request.form['correct_answer']
    score = 1 if selected_choice == correct_answer else 0
    return render_template('result.html', score=score)
    
if __name__ == '__main__':
    app.run(debug=True)
