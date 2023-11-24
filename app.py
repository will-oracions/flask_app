from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/tp")
def hello_world():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_data():
    username = request.form['username']
    members = ["Will", "Jeremy", "Perez", "Josephine", "Princesse"]
    isCold = True

    print(members)
    
    return render_template(
        'index.html',
        username=username,
        members=members,
        isCold=isCold
    )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")