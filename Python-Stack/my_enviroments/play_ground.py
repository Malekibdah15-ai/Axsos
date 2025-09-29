from flask import Flask  
 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
 

if __name__ == '__main__':
    app.run(debug=True)