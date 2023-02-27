from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'home'

@app.route('/portfolio')
def portfolio():
  return 'portfolio'