from flask import Flask,render_template,request
'''
It creates a instance of the flask class,
Which will be your WSGI(Webserver Gateway interface) application
'''
#Wsgi Application
app = Flask(__name__)

@app.route("/")
def welocme():
    return "welocme to flask app.This should be a great"

@app.route("/with_html")
def Html():
    return "<html><H1>Testing<H1><html>"

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

## Flask get and post operations
@app.route('/test',methods=['GET','POST'])
def Postinfo():
    if request.method =='POST':
       print("Method:-",request.method)
       print('first_name:-',request.form['fname'])
   
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)


