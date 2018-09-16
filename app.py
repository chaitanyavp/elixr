from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import sys
import davinci_caller as d

app = Flask(__name__)
CORS(app)

api_key = ""
customer_key = ""
tr_df = None

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/test', methods=["GET"])
def test():
    return "very good one"


@app.route('/company_spending', methods=["GET"])
def company_spending():
    return jsonify(d.get_company_spending(tr_df))


@app.route('/branch_spending', methods=["GET"])
def branch_spending():
    return jsonify(d.get_branch_spending(tr_df))


@app.route('/yearly_spending', methods=["GET"])
def yearly_spending():
    return jsonify(d.get_yearly_spending(tr_df))


@app.route('/monthly_spending', methods=["GET"])
def monthly_spending():
    return jsonify(d.get_monthly_spending(tr_df))


@app.route('/grocery_spending', methods=["GET"])
def grocery_spending():
    return jsonify(d.get_grocery_list(tr_df))


@app.route('/eatingout_spending', methods=["GET"])
def eatingout_spending():
    return jsonify(d.get_eatingout_list(tr_df))


@app.route('/points_steps', methods=["GET"])
def points_steps():
    points, steps = d.read_firebase(customer_key)
    return jsonify({"points": points, "steps": steps})


@app.route('/total_income', methods=["GET"])
def total_income():
    return jsonify({"points": d.get_income(customer_key, api_key)})


@app.route('/get_public_transportation', methods=["GET"])
def public_transportation():
    return jsonify({"result": d.get_public_transportation()})


@app.route('/get_groceries', methods=["GET"])
def get_groceries():
    return jsonify({"result": d.get_groceries()})


@app.route('/get_rest', methods=["GET"])
def get_rest():
    return jsonify({"result": d.get_rest()})


@app.route('/get_rec', methods=["GET"])
def get_rec():
    return jsonify({"result": d.get_rec()})


@app.route('/get_bank_total', methods=["GET"])
def get_bank_total():
    return jsonify({"result": d.get_bank_total(customer_key, api_key)})


@app.route('/json', methods=["POST"])
def json_example():
    json_dict = request.get_json()
    if json_dict is not None:
        print(request.mimetype, json_dict['good'], file=sys.stderr)
        print(type(json_dict['list']), json_dict['list'], file=sys.stderr)
        return "good"
    else:
        return "bad"


if __name__ == "__main__":
    api_key = d.get_api_key()
    customer_key = d.get_customer_key()
    tr_df = d.get_transaction_df(api_key, customer_key)
    app.run("127.0.0.1", "5000")
