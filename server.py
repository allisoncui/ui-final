from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from flask import session

import os
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def str_filter(value):
    return str(value)
    
app.jinja_env.filters['str'] = str_filter

quiz_questions = [
    {
        'question': 'You are given a vase that has a slight crack on the side. It costs $50 because it belongs to an antique collection. What would be your first comment to bargain the price?',
        'choices': [
            'I don’t care too much about antique vases. Could you lower the price to $30?',
            'There is a crack on the side of the vase, meaning it’s been used. Could you lower the price to $40?',
            'I’ll pay the full amount in cash if it is lowered to $30.',
            'Your nextdoor neighbor is selling a very similar vase for just $25.'
        ],
        'correct_answer': 'There is a crack on the side of the vase, meaning it’s been used. Could you lower the price to $40?'
    },
    {
        'question': 'What is an action you should avoid doing when negotiating?',
        'choices': [
            'Pointing out imperfections.',
            'Offering cash.',
            'Reverse auctioning.',
            'Being genuine.'
        ],
        'correct_answer': 'Reverse auctioning.'
    },
    {  # Note the comma before this line that separates the dictionary entries
        'question': 'You are at a local farmers market and find a vendor selling fresh apples. The vendor is asking for $5 per pound, but you\'ve noticed other stalls offering similar apples at lower prices. What\'s your next step to negotiate a better price?',
        'choices': [
            'Offer to buy in bulk if they lower the price to $3 per pound.',
            'Mention the lower prices at other stalls and ask if they can match the price.',
            'Walk away to see if the vendor offers a better deal before you leave.',
            'Pay the asking price because it supports local farmers.'
        ],
        'correct_answer': 'Mention the lower prices at other stalls and ask if they can match the price.'
    },
    {
    'question': 'During a car purchase negotiation, the seller insists on a price that is above your budget. What is the best approach to continue the negotiation?',
    'choices': [
        'Tell the seller bluntly that the price is too high and threaten to leave.',
        'Acknowledge the seller’s price, but share your research on lower prices for similar models elsewhere.',
        'Agree to the asking price and try to negotiate for additional perks like free servicing.',
        'Immediately agree to the price to avoid further negotiation.'
    ],
    'correct_answer': 'Acknowledge the seller’s price, but share your research on lower prices for similar models elsewhere.'
    },
    {
    'question': 'When trying to get a better deal on a vintage watch, the seller claims it’s a rare piece. How do you respond to strengthen your bargaining position?',
    'choices': [
        'Question the authenticity of the watch and ask for proof like certificates.',
        'Admit you’re not knowledgeable about watches and ask for a discount.',
        'Compliment the watch excessively to make the seller feel proud and then ask for a discount.',
        'Express skepticism about its rarity and suggest a lower price based on your observations.'
    ],
    'correct_answer': 'Express skepticism about its rarity and suggest a lower price based on your observations.'
    }
]
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
    session.setdefault('answers', {})  
    index = request.args.get('index', default=0, type=int)
    index_str = str(index)  # Convert index to string for session key usage

    if 'answers' not in session:
        session['answers'] = {}

    if index >= len(quiz_questions):
        return redirect(url_for('quiz_result'))

    question_data = quiz_questions[index]
    total_questions = len(quiz_questions)
    return render_template('quiz.html', question_data=question_data, index=index, index_str=index_str, total_questions=total_questions)




    
@app.route('/submit_answer/<int:index>', methods=['POST'])
def submit_answer(index):
    choice = request.form['choice']
    if 'answers' not in session:
        session['answers'] = {}
    session['answers'][str(index)] = choice

    # If not the last question, redirect to the next question
    if index + 1 < len(quiz_questions):
        return redirect(url_for('quiz', index=index + 1))

    # If it's the last question, calculate score and show results
    score = calculate_score(session['answers'])
    session.pop('answers', None)  # Clear the session answers
    return render_template('final_result.html', score=score, total_questions=len(quiz_questions))

def calculate_score(answers):
    score = 0
    for i, question in enumerate(quiz_questions):
        if str(i) in answers and answers[str(i)] == question['correct_answer']:
            score += 1
    return score




@app.route('/quiz/result', methods=['POST'])
def quiz_result():
    index = request.args.get('index', type=int, default=0)
    selected_choice = request.form['choice']
    correct_answer = request.form['correct_answer']
    
    # Initialize score in session if it doesn't exist
    if 'score' not in session:
        session['score'] = 0
    
    # Update score based on the current answer
    if selected_choice == correct_answer:
        session['score'] += 1
    
    # Move to the next question or finish quiz
    if index + 1 >= len(quiz_questions):
        total_score = session.pop('score', 0)  # Get total score and reset the session
        return render_template('final_result.html', score=total_score, total_questions=len(quiz_questions))
    else:
        return redirect(url_for('quiz', index=index + 1))

    
if __name__ == '__main__':
    app.run(debug=True)
