from flask import Flask

app = Flask(__name__)

@app.route('/home')
def welcome():
    return "I am abhishek"

if __name__ == '__main__':
    app.run(debug=True)