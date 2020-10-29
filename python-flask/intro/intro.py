from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome To Flask'

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s. Welcome to Flask' % name




if __name__ == '__main__':
    #app.run()
    app.run('0.0.0.0','6700',debug = True)
