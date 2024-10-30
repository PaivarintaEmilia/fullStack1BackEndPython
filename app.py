from flask import Flask
from flask_cors import CORS
from flask.cli import load_dotenv

from controllers import controller_user, controller_income

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

# Ohjelman käynnistäminen
if __name__ == '__main__':
    load_dotenv()
    app.run()
