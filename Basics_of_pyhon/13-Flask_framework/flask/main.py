from flask import Flask 


'''
It creates an instance of the flask class,
which will be yout WSGI
'''
app=Flask(__name__) 

@app.route('/') ## home page route
def welcome():
    return "<html><h1>HI I'm Mahadev</h1></html>"

@app.route("/index")
def welcome_index():
    return "Welcome to index page.This should be amazon course"

@app.route('/login')
def welocome_login():
    return "Welcome to login Page"

if __name__=="__main__":## entry piont
    app.run(debug=True)
