from flask import Flask, jsonify, request
from investment_manager import InvestmentManager

app = Flask(__name__)

investment_manager = InvestmentManager()

@app.route('/add_investment', methods=['POST'])
def add_investment():
    investment_data = request.get_json()
    investment_manager.add_investment(investment_data)
    return "Investment added successfully."

@app.route('/get_all_investments/<string:investment_type>', methods=['GET'])
def get_all_investments(investment_type):
    investments = investment_manager.get_all_investments(investment_type)
    return jsonify(investments)

if __name__ == '__main__':
    app.run(debug=False)
