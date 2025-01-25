from flask import Flask 


'''
It creates an instance of the flask class,
which will be yout WSGI
'''
app=Flask(__name__) 

@app.route('/') ## home page route
def welcome():
    return "Welcome to thsi flask.This should be amazon course"

@app.route("/index")
def welcome_index():
    return "Welcome to index page.This should be amazon course"


if __name__=="__main__":## entry piont
    app.run(debug=True)
