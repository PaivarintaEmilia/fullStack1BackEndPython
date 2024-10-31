from flask import Flask
from flask_cors import CORS
from flask.cli import load_dotenv

from controllers import controller_user, controller_income, controller_expense

# Flaskin luominen
app = Flask(__name__)
# Cors-tuki, sillä muuten tulee OPTIONS virheilmoitus
CORS(app)

# USERS ROUTET
# Front-endistä tuleva data on JSON muodossa, method POST ja sieltä tulee vain username ja password
@app.route('/users/<db_type>', methods=['POST'])
def get_one_user(db_type):
    print("App.py")
    return controller_user.get_user_by_username(db_type)



# INCOME ROUTET

# Haetaan data home-pagen total income tietoa varten
@app.route('/income/<db_type>/<user_id>', methods=['GET'])
def get_income(db_type, user_id):
    print("App.py")
    return controller_income.get_monthly_income_by_id(db_type, user_id)

# Lisätään uusi income
@app.route('/income/<db_type>', methods=['POST'])
def new_income(db_type):
    print("App.py")
    return controller_income.new_income(db_type)



# EXPENSE ROUTET
# Haetaan data Home-pagen total expense tietoa varten
@app.route('/expense/<db_type>/<user_id>', methods=['GET'])
def get_expense(db_type, user_id):
    print("App.py")
    return controller_expense.get_monthly_expense_by_id(db_type, user_id)

# Lisätään uusi expense
@app.route('/expense/<db_type>', methods=['POST'])
def new_expense(db_type):
    print("App.py")
    return controller_expense.new_expense(db_type)

# Ohjelman käynnistäminen
if __name__ == '__main__':
    load_dotenv()
    app.run()
