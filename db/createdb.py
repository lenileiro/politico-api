import os
from psycopg2 import connect
from datetime import datetime

def connect_to_db(config=None):
    db_name=''
    if config == 'testing':
        db_name = os.getenv('DATABASE_TEST_URL')
    else:
        db_name = os.getenv('DATABASE_URL')

    return connect(db_name)
    
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

def init_db(config=None):
    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    create_users_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database created successfully')


if __name__ == '__main__':
    init_db()