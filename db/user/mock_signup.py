from app.api.v2.models.auth import AuthModel
from collections import namedtuple
user = {
          "national_id": 32308961,
          "firstname": "john",
          "lastname": "Joe",
          "othername": "smith",
          "email": "johndoe@gmail.com",
          "isadmin": "False",
          "phone": "+254724862149",
          "password":"123456789",
          "passporturl": "https://demo.com/image.jpg"
      }
      
Params = namedtuple("Params", ["national_id", "firstname", "lastname", "othername", "email", "phone", "isadmin", "password", "passporturl"])
params = Params(user["national_id"], user["firstname"], user["lastname"], user["othername"], user["email"], user["phone"], user["isadmin"], user["password"], user["passporturl"])

def main():
  AuthModel.insert_user(params)
