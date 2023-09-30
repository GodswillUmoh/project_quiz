from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

# Load the quiz questions and answers from questions.py
from questions import questions

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        user_answer = request.form.get(question['id'])
        if user_answer == question['answer']:
            score += 1
        
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
