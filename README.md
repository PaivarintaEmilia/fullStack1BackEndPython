# Expense Tracker - Back-End

Tervetuloa Expense Tracker -ohjelman back-endiin! Tämä sovellus on rakennettu Flask-kirjastolla ja se käyttää PostgreSQL-tietokantaa. Sovelluksen avulla voit hallita tuloja ja menoja tehokkaasti.

## Vaatimukset

- Python 3.x
- Flask
- Flask-CORS
- Psycopg2 (PostgreSQL-tietokannan käyttöön)

## Asennus

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>


## Asenna vaatimukset

```
pip install -r requirements.txt
```

## Määritä ympäristömuuttujat

- tiedot löytyy .env.example tiedostosta

## Käynnistäminen

```
python app.py
```

- tai App.py tiedostosta


## Routet

### Käyttäjät

POST /users/<db_type>

Tämä reitti vastaanottaa JSON-muotoisen datan, jossa on käyttäjänimi ja salasana, ja palauttaa käyttäjän tiedot.

Tulojen käsittely
GET /income/<db_type>/<user_id>

Haetaan käyttäjän kuukausittaiset tulot.

POST /income/<db_type>

Lisää uusi tulo. JSON-body on seuraavanlainen:

```
{
    "user_id": 2,
    "income_amount": 200, 
    "note": "Back-end testi"
}
```

## Menojen käsittely

GET /expense/<db_type>/<user_id>

Haetaan käyttäjän kuukausittaiset menot.

POST /expense/<db_type>

Lisää uusi meno. JSON-body on seuraavanlainen:

```
{
    "user_id": 2,
    "category_id": 4,
    "expense_amount": 200,
    "note": "Back-end testi"
}
```

## Kategoriat

GET /expensecategory/<db_type>/<user_id>

Hakee kategoriat valikkoa varten.
