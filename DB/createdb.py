import os
from psycopg2 import connect
from datetime import datetime

def connect_to_db(config=None):

    if config == 'testing':
        db_name = os.getenv('DATABASE_TEST_URL')
    else:
        db_name = os.getenv('DATABASE_URL')

    host = os.getenv('DATABASE_HOST')
    user = os.getenv('DATABASE_USERNAME')
    password = os.getenv('DATABASE_PASSWORD')

    return connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )


def create_users_table(cur):
    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS politico;
        """)
    cur.execute(
        """CREATE TABLE IF NOT EXISTS politico.user (
            id SERIAL PRIMARY KEY NOT NULL,
            national_id INTEGER NOT NULL, 
            firstname VARCHAR (100) NOT NULL, 
            lastname VARCHAR (100) NOT NULL, 
            othername VARCHAR (100), 
            email VARCHAR (100) NOT NULL, 
            phone VARCHAR (100) NOT NULL, 
            isadmin VARCHAR (6) NOT NULL, 
            password VARCHAR (250) NOT NULL, 
            passporturl VARCHAR (100) NOT NULL, 
            created_at TIMESTAMP);""")

def mock_users_table(cur):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = {
        "national_id": 32308961,
        "firstname": "John",
        "lastname": "Joe",
        "othername": "smith",
        "email": "johndoe@gmail.com",
        "isadmin": "False",
        "phone": "+254724862149",
        "password":"pbkdf2:sha256:50000$y9DI0W56$dbc0ccc48dd099ebcafdf49be84273c81b3618fdbf7a1f67cb30bf9655a2ce38",
        "passporturl": "https://demo.com/image.jpg",
        "created_at": created_at
    }

    admin = {
        "national_id": 22463235,
        "firstname": "Kevin",
        "lastname": "Joe",
        "othername": "smith",
        "email": "kevindoe@gmail.com",
        "isadmin": "False",
        "phone": "+254724862149",
        "password":"pbkdf2:sha256:50000$y9DI0W56$dbc0ccc48dd099ebcafdf49be84273c81b3618fdbf7a1f67cb30bf9655a2ce38",
        "passporturl": "https://demo.com/image.jpg",
        "created_at": created_at
    }
    sql = """
            INSERT INTO politico.user
            (national_id, firstname, lastname, othername, 
             email, phone, isadmin, password, passporturl,created_at)
            VALUES (%(national_id)s, %(firstname)s, %(lastname)s, %(othername)s, 
            %(email)s, %(phone)s, %(isadmin)s,%(password)s,%(passporturl)s, %(created_at)s)
            """

    cur.execute(sql, user)
    cur.execute(sql, admin)

def main(config=None):
    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS users CASCADE""")

    create_users_table(cur)
    mock_users_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database created successfully')


if __name__ == '__main__':
    main()
