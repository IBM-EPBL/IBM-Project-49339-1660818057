from flask import Flask,render_template 

app=Flask(__name__)


@app.route('/')
@app.route('/signin')
def signin():
    return render_template('signin.html')

   
if __name__ =="__main__":
    app.run(debug=True)
