import os
from psycopg2 import connect


def connect_to_db(config=None):

    if config == 'testing':
        db_name = os.getenv('TEST_DB')
    else:
        db_name = os.getenv('DB_NAME')

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')

    return connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )
    
def create_users_table(cur):
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


def main(config=None):
    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS users CASCADE""")
    cur.execute("""DROP TABLE IF EXISTS entries CASCADE""")

    create_users_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database created successfully')


if __name__ == '__main__':
    main()
