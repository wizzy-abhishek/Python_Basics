from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form1", methods=['POST','GET'])
def form():
    if request.method == 'POST':
        data = request.form['name']
        return f'Hiiiii {data}'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)