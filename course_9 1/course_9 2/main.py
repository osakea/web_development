from random import randint 
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after


def index():
    global quiz, last_question
    max_quiz = 3
    # if student wrote get_quiz_count(), specify max_quiz    = get_quiz_count[0]
    session['quiz'] = randint(1, max_quiz)
    # if student wrote ger_quiz_count(), specify session['quiz'] = get_random_quiz-id()
    session['last_question']= 0
    return '<a href="/test">Test</a>'

def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    
    else: 
        session['last_question'] = result[0]
        return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'
    
def result():
    return "that's all"

# creating a web app object:
app = Flask(__name__)
app.add_url_rule('/', 'index', index) 
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
#encrypt key
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'


if __name__ == '__main__':
    app.run()