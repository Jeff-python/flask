from flask import Flask, jsonify, render_template
from random import randint

app = Flask(__name__)

@app.route('/api/add/<n1>/<n2>', methods =['GET'])
def add(n1,n2):
    answer ={"answer":(int(n1)+int(n2))}
    return jsonify(answer)

@app.route('/api/subtract/<n1>/<n2>', methods =['GET'])
def subtract(n1,n2):
    answer = {"answer":(int(n1)-int(n2))}
    return jsonify(answer)

@app.route('/api/multiply/<n1>/<n2>', methods =['GET'])
def multiply(n1,n2):    
    answer ={"answer":int(n1)*int(n2)}
    return jsonify(answer)

@app.route('/api/divide/<n1>/<n2>', methods =['GET'])
def divide(n1,n2):    
    answer = {"answer": int(n1)/int(n2)}
    return jsonify(answer)

# Write a flask route that renders a simple html document 
# with 6 random numbers between 1-6 inside `<p>` tags

# @app.route('/random/', methods =['GET'])
# def random(): 
#     empty =" "
#     for i in range(5):
#         empty += str(randint(1,6))
#     return str(empty)
# "<p>" + random_num + "</p>"

#     for i in range(5):
#         return str(i)

@app.route('/random/', methods =['GET'])
def random(): 
    for i in range(6):
        i = str(randint(1,6))
        return "<p>" + i + "</p>"
        # return (f'<p>{i}</p>')
# <p>4</p>
# <p>5</p>
# <p>6</p>
# <p>2</p>
# <p>1</p>
# <p>1</p>


# @app.route('/random/<p>', methods =['GET'])
# def random(p):  
#     empty =[] 
#     for i in range(5):
#         empty.append(str(randint(1,6)))
#         (",").join(empty)
#         return str(empty)

@app.route('/cowsay/<string>', methods =['GET'])
def cowsays(string):    
    cowsays = {string : "Moooo!"}
    return jsonify(cowsays)

#  Write a flask app that takes the route `/moby/<int>` 
#  that returns a string of the N'th word in the text of moby dick
@app.route('/moby/<num>', methods =['GET'])
def moby(num):  
    lst = []
    line = render_template('mobydick.txt').split()
    for i in line:
        lst.append(i)
    return str(lst[int(num)-1])    
    



    

if __name__ == "__main__":
    app.run(debug = True) 