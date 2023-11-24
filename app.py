from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_data():
    username = request.form['username']
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)