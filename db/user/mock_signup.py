from db.models import AuthModel
from collections import namedtuple
user = {
        "national_id": 222222,
        "firstname": "John",
        "lastname": "Joe",
        "othername": "smith",
        "email": "johndoe@gmail.com",
        "isadmin": "False",
        "phone": "+254724862149",
        "password":"123",
        "passporturl": "demo.com/image.jpg"
      }
      
Params = namedtuple("Params", ["national_id", "firstname", "lastname", "othername", "email", "phone", "isadmin", "password", "passporturl"])
params = Params(user["national_id"], user["firstname"], user["lastname"], user["othername"], user["email"], user["phone"], user["isadmin"], user["password"], user["passporturl"])

def main():
  AuthModel.insert_user(params)
