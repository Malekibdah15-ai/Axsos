from flask import Flask, render_template



app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template('index.html', number = 64)


if __name__ == "__main__":
    app.run(debug=True)