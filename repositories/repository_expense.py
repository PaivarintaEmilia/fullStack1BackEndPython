import models
from datetime import datetime, timedelta


class ExpenseRepository:

    def __init__(self, connection):
        self.connection = connection

    # Hae käyttäjä usernamen perusteella
    # Tämä tapahtuma on FE puolella, kun käyttäjä koittaa kirjautua sisään
    def get_monthly_expense_by_id(self, user_id):

        # Array mihin tallennetaan luokan instanssit
        all_amounts = []

        print("Repo / Expense")
        print("Repo / user_id: ", user_id)


        # Haetaan kuukauden ensimmäinen päivä
        first_day_month = datetime.today().replace(day=1).date()
        print("Repo / first_day: ", first_day_month)
        # Haetaan kuukauden viimeinen päivä

        now = datetime.now()
        # Kuukausi ja vuosi
        month = now.month
        print("Repo / month: ", month)
        year = now.year
        print("Repo / year: ", year)

        # Selvitetään kuun viimeinen päivä ja tallennetaan se muuttujaan
        if month == 12:
            last_day_month = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day_month = datetime(year, month + 1, 1) - timedelta(days=1)

        last_day_month = last_day_month.date()

        print("Repo / last_day: ", last_day_month)

        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM expense WHERE user_id = %s AND expense_date BETWEEN %s AND %s',
                           (user_id, first_day_month, last_day_month))
            result = cursor.fetchall()

            for amounts in result:
                all_amounts.append(models.Expense(amounts[1], amounts[2], amounts[3], amounts[4], amounts[0]))


            print("Repo all_amounts: ", all_amounts)



            return all_amounts

    # LISÄTÄÄN UUSI INCOME, KUN KÄYTTÄJÄ ON SAANUT TULOJA
    def insert_expense(self, sent_data):

        print("Repo / Expense")
        print("Repo / sent_data", sent_data)

        # PÄIVÄN MUUTTUJIEN MÄÄRITTÄMINEN

        # Tarvitaan tämä päivä, jotta voidaan lisätä samalla päivällä tieto tietokantaan
        date = datetime.now().date()

        print("Repo / todays day: ", date)

        # TIETOKANTAKYSELY

        with self.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO expense (user_id, category_id, expense_amount, expense_date, note) VALUES (%s, %s, %s, %s, %s) RETURNING expense_id',
                (sent_data['user_id'], sent_data['category_id'], sent_data['expense_amount'], date, sent_data['note']))
            self.connection.commit()

            expense_id = cursor.fetchone()[0]
            print("repo/postgres/expense_id", expense_id)

            if expense_id > 0:
                # Haetaan lisätyn incomen tiedot
                cursor.execute("SELECT * FROM expense WHERE expense_id = %s", (expense_id,))
                new_expense = cursor.fetchone()

                if new_expense:
                    print("Create expense repo / instanssi ",
                          models.Expense(new_expense[1], new_expense[2], new_expense[3], new_expense[4], new_expense[5], new_expense[0]))
                    return models.Expense(new_expense[1], new_expense[2], new_expense[3], new_expense[4], new_expense[5], new_expense[0])
            else:
                return None

