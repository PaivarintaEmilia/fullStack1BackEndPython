from decorators.db_connection import DbBaseDecoration
from repositories.repository_income import IncomeRepository

from flask import jsonify, request



# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    print("Get repo in controller")
    # Palautetaan Repositoryn instanssi
    return IncomeRepository(connection)





# FUNKTIOT TIEDON VÄLITTÄMISEEN REPON JA APP.PY VÄLILLÄ

# Haetaan yksi käyttäjä usernamen perusteella
def get_monthly_income_by_id(db_type, user_id):


    print("Controller alku income")
    repository = get_repository(db_type)

    # Otetaan talteet POST-requestin mukana lähetetty data
    # data = request.get_json()

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    income_records = repository.get_monthly_income_by_id(user_id)

    print("Controller / income reposta: ", income_records[0].user_id) # 2
    print("Controller / income reposta: ", income_records[0].income_id) # Opintotuki
    print("Controller / income reposta: ", income_records[0].income_amount) #
    print("Controller / income reposta: ", income_records[0].income_date)
    print("Controller / income reposta: ", income_records[0].note)
    # print("Controller / user.username / data reposta: ", user.username)
    # print("Controller / user.id / data reposta: ", user.id)


    total_income = 0
    for amount in income_records:
        total_income += amount.income_amount

    print("Testi: ", total_income)



    return jsonify({"total_income": total_income}), 200
'''
    amounts_json = []
    for amount in income_records:
        print("COntroller / inside lood / income_id: ", amount.income_id)
        amounts_json.append({
            'income_id': amount.income_id,
            'user_id': amount.user_id,
            'income_amount': amount.income_amount,
            'income_date': amount.income_date,
            'note': amount.note,
        })
        
'''
