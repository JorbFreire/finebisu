from os import getenv
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
import json

from .controllers.transactionsController import transactionsController
from .services.update_databae import update_datebase

load_dotenv()
env = getenv

app = Flask(__name__)
CORS(app)

is_database_updated = False


@app.route("/", methods=['GET'])
def ping():
    return {"ping": "pong"}


@app.route("/transactions", methods=['GET'])
def getTransactions():
    if not is_database_updated:
        nu = update_datebase(env("CPF"), env("PASSWORD"))
        transactions = transactionsController.show(nu)

        transactions_json = json.dumps(transactions, indent=4)
        with open("card_history.json", "w") as outfile:
            outfile.write(transactions_json)

        return {"transactions": transactions}
