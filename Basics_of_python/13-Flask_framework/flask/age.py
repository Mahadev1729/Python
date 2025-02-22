from flask import Flask,render_template

app=Flask(__name__)

@app.route('/vote/<int:age>')
def vote(age):
    ouput=""
    if age>=18:
        ouput="Eligible"
    else:
        ouput="Not Eligible"    
    return render_template('vote.html',results=ouput)
if __name__=="__main__":
    app.run(debug=True)
