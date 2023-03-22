from flask import Flask
from flask_cors import CORS
import environ

from .controllers.transactionsController import transactionsController
from .services.update_databae import update_datebase

env = environ.Env()
environ.Env.read_env()

app = Flask(__name__)
CORS(app)

is_database_updated = True

@app.route("/", methods=['GET'])
def ping():
  return { "ping": "pong" }
    
@app.route("/transactions", methods=['GET'])
def getTransactions():
  if not is_database_updated:
    update_datebase(env("CPF"), ("PASSWORD"))
    transactions = transactionsController.show()
    return { "transactions": transactions }
