from flask import Flask

app = Flask(__name__)

#from worldbankapp import routes
@app.route('/')
@app.route('/index')
def index():
    return "Hello Heroku Flask 0101"

   

if __name__ == '__main__':
    app.run()