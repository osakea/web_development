#your code is here

from flask import Flask, url_for, redirect
import sqlite3

def index():
    # establish a connection to the database and send a req
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()

    # When processing a req, consider a few options:
    # 1 - there is no data on artist born in the specified year in the database
    if len(data) == 0:
        return "There is no data in the database about artist born in  " + str(year) + 'year'
    
    #2 - there is only one artist born in the specified year
    elif len(data) == 1:
        return 'In ' + str(year) + 'year was born (born)' + data[0][0]
    
    #3 - several artists were born in specified year
    else:
        result = '<h3>List of artist born in ' + str(year) + ' year:</h3><ol>'
        for person in data:
            result += '<li>' + str(person[1])  + '</li>'
        result += '</ol>'
    return result

# the requested year of birth will be stored in global variable 
year = int(input("Enter the artist's year of birth "))
app = Flask(__name__)
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    #starting the web server
    app.run(debug=True)
