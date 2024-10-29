from decorators.postgres_connections import PostgresConnection

# Tarkoituksena, että tänne voi lisätä vaihtoehdoiksi uusia tietokantoja halutessa.
class DbBaseDecoration:

    @staticmethod
    def get_connection(db_type):
        if db_type == 'postgres':
            return PostgresConnection().get_postgres_connection()
        else:
            raise ValueError("Väärä valittu tietokantatyyppi.")
