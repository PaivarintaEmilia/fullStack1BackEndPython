import models
from datetime import datetime, timedelta


class IncomeRepository:

    def __init__(self, connection):
        self.connection = connection

    # Hae income iser_id:n perusteella
    # Tämä tapahtuma on FE puolella, kun käyttäjä koittaa kirjautua sisään
    def get_monthly_income_by_id(self, user_id):

        # Array mihin tallennetaan luokan instanssit
        all_amounts = []

        print("Repo / Income")
        print("Repo / user_id: ", user_id)

        # PÄIVÄN MUUTTUJIEN MÄÄRITTÄMINEN

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

        # TIETOKANTAKYSELY

        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM income WHERE user_id = %s AND income_date BETWEEN %s AND %s',
                           (user_id, first_day_month, last_day_month))
            result = cursor.fetchall()

            for amounts in result:
                all_amounts.append(models.Income(amounts[1], amounts[2], amounts[3], amounts[4], amounts[0]))

            #print("Repo databasen income_id: ", result[0])
            #print("Repo databasen user_id: ", result[1])
            #print("Repo databasen income_amount: ", result[2])
            #print("Repo databasen income_date: ", result[3])
            #print("Repo databasen note: ", result[4])
            print("Repo all_amounts: ", all_amounts)

            # PALAUTETAAN AINA LUOKAN INSTANSSI
            return all_amounts


    # LISÄTÄÄN UUSI INCOME, KUN KÄYTTÄJÄ ON SAANUT TULOJA
    def insert_income(self, sent_data):

        print("Repo / Income")
        print("Repo / sent_data", sent_data)

        # PÄIVÄN MUUTTUJIEN MÄÄRITTÄMINEN

        # Tarvitaan tämä päivä, jotta voidaan lisätä samalla päivällä tieto tietokantaan
        date = datetime.now().date()

        print("Repo / todays day: ", date)

        # TIETOKANTAKYSELY

        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO income (user_id, income_amount, income_date, note) VALUES (%s, %s, %s, %s) RETURNING income_id',
                           (sent_data['user_id'], sent_data['income_amount'], date, sent_data['note']))
            self.connection.commit()

            income_id = cursor.fetchone()[0]
            print("repo/postgres/income_id", income_id)

            if income_id > 0:
                # Haetaan lisätyn incomen tiedot
                cursor.execute("SELECT * FROM income WHERE income_id = %s", (income_id,))
                new_income = cursor.fetchone()

                if new_income:
                    print("Create income repo / instanssi ", models.Income(new_income[1], new_income[2], new_income[3], new_income[4], new_income[0]))
                    return models.Income(new_income[1], new_income[2], new_income[3], new_income[4], new_income[0])
            else:
                return None



