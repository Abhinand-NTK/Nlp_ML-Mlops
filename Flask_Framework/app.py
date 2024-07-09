from flask import Flask
'''
It creates a instance of the flask class,
Which will be your WSGI(Webserver Gateway interface) application
'''
#Wsgi Application
app = Flask(__name__)

@app.route("/")
def welocme():
    return "welocme to flask app.This should be a great"



if __name__ == '__main__':
    app.run(debug=True)


