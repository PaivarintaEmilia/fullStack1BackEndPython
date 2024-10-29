import models

class UserRepository:

    def __init__(self, connection):
        self.connection = connection


    # Hae käyttäjä usernamen perusteella
    # Tämä tapahtuma on FE puolella, kun käyttäjä koittaa kirjautua sisään
    def get_user_by_username(self, login_data):
        print("Repo")
        print("Repo / login_data: ", login_data)
        print("Repo / login_data.username: ", login_data['username'])
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE username = %s', (login_data['username'],))
            result = cursor.fetchone()

            print("Repo frontin password: ", login_data['password'])
            print("Repo databasen password: ", result[2])
            print("Repo databasen id: ", result[0])
            print("Repo databasen username: ", result[1])


            # Tarkistetaan password tässä, kun en oo satavarma missä pitäisi tarkistaa
            if login_data['password'] == result[2]:
                print("Get user by id luokan instanssi? ", models.User(result[1], result[2], result[0]))
                return models.User(result[1], result[2], result[0])
            else:
                return None


