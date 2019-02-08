# Badges

[![Build Status](https://api.travis-ci.org/lenileiro/politico-api.svg?branch=develop)](https://travis-ci.org/lenileiro/politico-api) 
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/politico-api?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2ba7d88ba0b45189d58fd361e33cea6)](https://www.codacy.com/app/lenileiro/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lenileiro/politico-api&amp;utm_campaign=Badge_Grade)

## Politico-api

Backend service where admin and citizen user can:
 Create a political party.
 Get all political parties.
 Get a specific political party.
 Edit a specific political party.
 Delete a particular party.
 Create a political office.
 Get all political offices.
 Get a specific political office.

### Description
Politico enables citizens give their mandate to politicians running for different government offices  while building trust in the process through transparency.

### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures

### Git hub Link
Please click [Github Link](https://github.com/lenileiro/politico-api/tree/develop) to view api the hosted source code on github.


### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | /api/v1/parties                                 |End point to create a party       |
| GET   | /api/v1/parties/                                  | Endpoint to get all parties       |
| GET   | /api/v1/parties/<int:party-id>                                   | End point to get a specific political party               |
| DELETE    | /api/v1/parties/<int:party-id>                                   | Delete a specific party                 |
| PATCH    | /api/v1/parties/<int:party-id>/name                 | Update a specific party name             |
| GET    | /api/v1/offices                | Get all offices      |
| POST   | /api/v1/offices       | Post an office        |
| GET    | /api/v1/offices/<int:office-id>    | Get a specific office          |

### Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python web microframework)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)
- [Pylint](https://www.pylint.org/) (Linting library)
- [Pip3](https://pypi.org/project/pip/) (Python package installer)


### Getting Started:

**To start the app, please follow the instructions below:**

**On your terminal:**

Install pip:
Install
Install sudo apt-get install python-pip
Install
- Clone this repository:

        $ git clone https://github.com/Nduhiu17/politico-server.git

- Get into the root directory:

        $ cd politico-server/

- Install virtual enviroment:

        $ python3.6 -m venv virtual

- Activate the virtual environment:

        $ source virtual/bin/activate
  
- Install requirements

        $ pip install -r requirements.txt



- Run the app by:

        $ python manage.py server

### Running the tests

Export server's secret key to the environment by:
     $ export SECRET_KEY='set-your-secret-key-here'


Run the tests by:

    $ pytest
