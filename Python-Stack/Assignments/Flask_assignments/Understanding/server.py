from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world!"

@app.route('/champion')
def page():
    return "champion"
@app.route("/say/<name>")
def say(name):
    return f"hi {name}"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return word * num

if __name__=="__main__":
    app.run(debug=True)
    
    
