from flask import Flask,jsonify
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

#create instaces
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

#create dictionary for users
USER = {
   "User": "password"
}

tickers = ["AAPL","MSFT","GOOG","AMZN","FB","TSLA","NVDA","JPM","BABA","JNJ","WMT","PG","PYPL","DIS","ADBE","PFE","V","MA","CRM","NFLX"]

prices = ["154.30", "3478.05"]

class ticker():
  def __init__(self, ticker):
    self.ticker = ticker

class price():
  def __init__(self, price):
    self.price = price

tickers.append(ticker(tickers[0]))
prices.append(price(prices[0]))

@auth.verify_password
def verify(username, password):
   if not (username and password):
       return False
   return USER.get(username) == password

class index(Resource):
   @auth.login_required
   def get(self):
       return jsonify({"symbol" : tickers[0], "price" : prices[0]})

api.add_resource(index,"/")


if __name__=="__main__":
   app.run(port=5000,debug=True)