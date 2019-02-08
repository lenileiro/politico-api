# Badges

[![Build Status](https://api.travis-ci.org/lenileiro/politico-api.svg?branch=develop)](https://travis-ci.org/lenileiro/politico-api) 
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/politico-api?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2ba7d88ba0b45189d58fd361e33cea6)](https://www.codacy.com/app/lenileiro/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lenileiro/politico-api&amp;utm_campaign=Badge_Grade)

## Politico-api-v1
Politico-api-v1 is collection of API endpoint that admin and citizen user store through data structure.


### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures

### Github Link
Please click [Github Link](https://github.com/lenileiro/politico-api/tree/develop) to view api the hosted source code on github.

### Heroku Link
Please click [Heroku Link](https://politico-v1-api.herokuapp.com/api/v1) to view api documentation and heroku api link


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


## Installation

Clone this repository:

    ```bash
    #!/bin/bash
    $ git clone https://github.com/lenileiro/politico-api.git
    ```

CD into the project folder on your machine

    ```bash
    #!/bin/bash
    $ cd politico-api
    $ pip install virtualenv
    ```

Create a virtual environment

   ```bash
    #!/bin/bash
    $ virtualenv venv
    ```

Activate the virtual environment

    ```bash
    #!/bin/bash
    $ source venv/bin/activate
    ```

Install the dependencies from the requirements file

    ```bash
    #!/bin/bash
    $ pip install -r requirements.txt
    ```

Run the application

    ```bash
    #!/bin/bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    PYTHONDONTWRITEBYTECODE=1 flask run
    ```

Run test

    ```bash
    #!/bin/bash
    PYTHONDONTWRITEBYTECODE=1 python -m pytest
    ```


### author
[Anthony Leiro](https://twitter.com/AnthonyLeni)