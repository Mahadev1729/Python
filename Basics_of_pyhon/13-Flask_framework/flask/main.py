from flask import Flask,render_template


'''
It creates an instance of the flask class,
which will be yout WSGI
'''
app=Flask(__name__) 

@app.route('/') ## home page route
def welcome():
    return render_template("home.html")

@app.route("/index")
def welcome_index():
    return render_template("index.html")

@app.route('/login')
def welocome_login():
    return "Welcome to login Page"

if __name__=="__main__":## entry piont
    app.run(debug=True)
