from decorators.db_connection import DbBaseDecoration
from repositories.repository_expense import ExpenseRepository

from flask import jsonify, request


# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    print("Get repo in controller")
    # Palautetaan Repositoryn instanssi
    return ExpenseRepository(connection)


# FUNKTIOT TIEDON VÄLITTÄMISEEN REPON JA APP.PY VÄLILLÄ

# Haetaan kaikki expense_amount summat id: perusteella
def get_monthly_expense_by_id(db_type, user_id):
    print("Controller alku expense")
    repository = get_repository(db_type)

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    expense_records = repository.get_monthly_expense_by_id(user_id)

    print("Controller / income reposta: ", expense_records[0].user_id)  # 2
    print("Controller / income reposta: ", expense_records[0].expense_id)  # Opintotuki
    print("Controller / income reposta: ", expense_records[0].expense_amount)  #
    print("Controller / income reposta: ", expense_records[0].expense_date)
    print("Controller / income reposta: ", expense_records[0].note)
    # print("Controller / user.username / data reposta: ", user.username)
    # print("Controller / user.id / data reposta: ", user.id)

    total_expense = 0
    for amount in expense_records:
        total_expense += amount.expense_amount

    print("Testi: ", total_expense)

    return jsonify({"total_expense": total_expense}), 200


# Lisätään expense
def new_expense(db_type):
    try:

        print("Controller alku income")
        repository = get_repository(db_type)

        # Otetaan talteet POST-requestin mukana lähetetty data
        data = request.get_json()
        print("Controller / data: ", data)

        # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
        expense_records = repository.insert_expense(data)

        # Saadaa palautuksena classin instanssi, jossa on lisätyn incomen tiedot
        print("Controller / expense_records: ", expense_records)

        if expense_records:
            # Palautetaan ok ilmoitus
            return jsonify("Expense Created Successfully"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
