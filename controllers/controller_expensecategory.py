from decorators.db_connection import DbBaseDecoration
from repositories.repository_expense import ExpenseRepository

from flask import jsonify, request

from repositories.repository_expensecategory import ExpenseCategoryRepository


# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    print("Get repo in controller")
    # Palautetaan Repositoryn instanssi
    return ExpenseCategoryRepository(connection)


# FUNKTIOT TIEDON VÄLITTÄMISEEN REPON JA APP.PY VÄLILLÄ

# Haetaan expensecategory-taulusta tiedot id:n perusteella ja frontille lähetetään category_id ja category_name
def get_expense_categories_by_id(db_type, user_id):
    print("Controller alku expensecategory")
    repository = get_repository(db_type)

    # Kutsutaan repo instanssin get_expense_categories_by_id-metodia ja haetaan kaikki valitut categoryt
    expense_categories = repository.get_expense_categories_by_id(user_id)

    print("Controller / Category reposta: ", expense_categories[0].category_id)  #
    print("Controller / Category reposta: ", expense_categories[0].user_id)  #
    print("Controller / Category reposta: ", expense_categories[0].category_name)  #
    print("Controller / Category reposta: ", expense_categories[0].user_defined)


    categories_response = []
    for item in expense_categories:
        categories_response.append({
            "categoryId": item.category_id,
            "categoryName": item.category_name
        })

    print("Testi: ", categories_response)

    return jsonify({"Category_listing": categories_response}), 200

