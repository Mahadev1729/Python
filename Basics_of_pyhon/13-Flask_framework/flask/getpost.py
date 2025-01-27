from flask import Flask,render_template

app=Flask(__name__) 

@app.route("/start")
def welcome_start():
    return render_template("start.html")

@app.route('/home') ## home page route
def welcome():
    return render_template("home.html")

@app.route("/index")
def welcome_index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def welocome_login():
    return "Welcome to login Page"

if __name__=="__main__":## entry piont
    app.run(debug=True)
