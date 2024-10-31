import models


class ExpenseCategoryRepository:

    def __init__(self, connection):
        self.connection = connection

    # Hae expensecategory-taulusta user_defined = false ja id:n perusteella
    def get_expense_categories_by_id(self, user_id):

        # Array mihin tallennetaan luokan instanssit
        all_categories = []

        print("Repo / ExpenseCategory")
        print("Repo / user_id: ", user_id)


        # TIETOKANTAKYSELY

        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM expensecategory WHERE user_defined = false OR user_id = %s',
                           (user_id,))
            result = cursor.fetchall()

            for items in result:
                all_categories.append(models.ExpenseCategory(items[1], items[2], items[3], items[0]))

            #print("Repo databasen income_id: ", result[0])
            #print("Repo databasen user_id: ", result[1])
            #print("Repo databasen income_amount: ", result[2])
            #print("Repo databasen income_date: ", result[3])
            #print("Repo databasen note: ", result[4])
            print("Repo all_categories: ", all_categories)

            # PALAUTETAAN AINA LUOKAN INSTANSSI
            return all_categories



