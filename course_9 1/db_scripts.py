import sqlite3
db_name = 'quiz.sqlite'
conn = None
curor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' delete all tables '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz(
       id INTEGER PRIMARY KEy,
       name VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS questions(
       id INTEGER PRIMARY KEY,
       question VARCHAR,
       answer VARCHAR,
       wrong1 VARCHAR,
       wrong2 VARCHAR,
       wrong3 VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
       id INTEGER PRIMARY KEY,
       quiz_id INTEGER,
       question_id INTEGER,
       FOREIGN KEY (quiz_id) REFERENCES quiz(id),
       FOREIGN KEY (question_id) REFERENCES questions(id))''')
    close()

def add_questions():
    questions = [
        ('How many months in a year have 28 days?', 'All', 'One', 'None', 'Two'),
        ('What will the green cliff look like if it falls into the Red Sea?', 'Wet', 'Red', 'Will not change', 'Purple'),
        ('Which hand is better to stir the tea with?', 'Spoon', 'Right', 'Left', 'Any'),
        ('What has no length, depth, width, or height, but can be measured?', 'Time', 'Stupidity', 'Sea', 'Air'),
        ('When is it possible to draw out water with a net?', 'When the water is frozen', 'When there are no fish', 'When the goldfish swim away', 'When the net breaks'),
        ('What is bigger than an elephant and weighs nothing?', 'Shadow of elephant', 'A balloon', 'A parachute', 'A cloud')
    ]
    open()
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('Own game', ),
        ('Who wants to be a millionaire?', ),
        ('The smartest', )]
    
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys = on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    answer = input("Add a link (y, n)")
    while answer != 'n':
        quiz_id = int(input("quiz id: "))
        question_id = int(input("question id: "))
        cursor.execute(query, (quiz_id, question_id))
        conn.commit()
        answer = input("Add a link (y, n)")
    close()

def get_question_after(question_id = 0, quiz_id=1):
    ''' returns the next question after the question with the passed ID
    for the first question, the default value is passed'''
    open()
    query = '''
    SELECT quiz_content.id, questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
    FROM questions, quiz_content
    WHERE quiz_content.question_id == questions.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id'''
    cursor.execute(query, (question_id, quiz_id))
    result = cursor.fetchone()
    close()
    return result

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('questions')
    show('quiz')
    show('quiz_content')

def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    add_links()
    show_tables()

if __name__ == "__main__":
    main()

