from decorators.db_connection import DbBaseDecoration
from models import User
from repositories.repository_user import UserRepository

from flask import jsonify, request
import jwt
import datetime

# Siirrä kokeilujen jälkeen .env filuun
SECRET_KEY = 'dfkfmkemffghde83486yjnhdj'


# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    print("Get repo in controller")
    # Palautetaan Repositoryn instanssi
    return UserRepository(connection)


# Luodaan JWT token
def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expiration
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


# FUNKTIOT TIEDON VÄLITTÄMISEEN REPON JA APP.PY VÄLILLÄ

# Haetaan yksi käyttäjä usernamen perusteella
def get_user_by_username(db_type):
    try:
        print("Controller alku")
        repository = get_repository(db_type)

        # Otetaan talteet POST-requestin mukana lähetetty data
        login_data = request.get_json()

        # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
        user = repository.get_user_by_username(login_data)

        print("Controller / user / data reposta: ", user)
        print("Controller / user.username / data reposta: ", user.username)
        print("Controller / user.id / data reposta: ", user.id)

        if user:
            selected_user = user.to_json()
            print("User/to_json controller ", selected_user)
            token = create_token(selected_user['id'])
            print("Controller / token ", token)
            return jsonify({'token': token, 'user_id': selected_user['id']})
    except Exception as e:
        return jsonify({'User not found': str(e)}), 500
