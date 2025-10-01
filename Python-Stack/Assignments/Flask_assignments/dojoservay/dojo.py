from flask import Flask, render_template, request

 
app = Flask(__name__)  

@app.route('/') 
def table():
    
    return render_template('login.html')

@app.route('/users', methods=['post']) 
def create_user():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    Language = request.form['Language']
    comment = request.form['comment']
    return render_template('SHOW.html')
    

    
 
 
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
