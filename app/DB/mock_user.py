import psycopg2
from datetime import datetime
import os

DATABASE_URI = os.getenv('DATABASE_URL','')
con = psycopg2.connect(DATABASE_URI)


cur = con.cursor()


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


class Mock:
    def __init__(self):
        self.con = con
        self.cur = cur

    def create_user(self, user):
        query = """
            INSERT INTO politico.user
            (national_id, firstname, lastname, othername, 
             email, phone, isadmin, password, passporturl,created_at)
            VALUES (%(national_id)s, %(firstname)s, %(lastname)s, %(othername)s, 
            %(email)s, %(phone)s, %(isadmin)s,%(password)s,%(passporturl)s, %(created_at)s)
            """
        self.cur.execute(query, user)
        self.con.commit()

mock = Mock()
mock.create_user(user)
mock.create_user(admin)
