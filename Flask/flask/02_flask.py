from flask import Flask

app = Flask(__name__)

@app.route('/home')
def welcome():
    return "<html> " \
    "<head> " \
    "<h1> Hello from h1 </h1>" \
    "<br>" \
    "<h2> Hello from h2 </h2>" \
    "</head>" \
    "</html>"

if __name__ == "__main__":
    app.run(port=8080, debug=True)