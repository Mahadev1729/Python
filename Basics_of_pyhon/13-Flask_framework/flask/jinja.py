## building url dynamically
## variable rule
## jinga 2 engine

##  Jinga2 Template Engine
'''
{{}} expressins to print ouput in html
{%....%}  condition,for loop
{#....#}  this is for comments
'''

from flask import Flask,render_template,request

app=Flask(__name__) 

@app.route("/start")
def welcome_start():
    return render_template("start.html")

@app.route('/') ## home page route
def welcome():
    return render_template("home.html")

@app.route("/index",methods=['GET'])
def welcome_index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def welocome_login():
    return "Welcome to login Page"

# @app.route('/form',methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}'
#     return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')
## variable role

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
        
    exp={'score':score,"res":res}        
    
    return render_template('result.html',results=res)## act like data source

#building url dynma
   

if __name__=="__main__":## entry piont
    app.run(debug=True)
