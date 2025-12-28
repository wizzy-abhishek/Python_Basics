from flask import Flask
import sqlite3

conn = sqlite3.Connection("mydb.db")
curs = conn.cursor()

app = Flask(__name__)

@app.route('/')
def welcome():
    return f"<html> " \
    "<head> " \
    "<h1> Hello from h1 </h1>" \
    "<br>" \
    "<h2> Hello from h2 </h2>" \
    "</head>" \
    "</html>"

curs.execute("Select * from employee")
rows = curs.fetchall()

@app.route('/home')
def mytask():
    a = ""
    for row in rows:
        a += " ".join(str(v) for v in row) + " "
    return a

if __name__ == "__main__":
    app.run(port=8080, debug=True)