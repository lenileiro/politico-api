# Badges

[![Build Status](https://api.travis-ci.org/lenileiro/politico-api.svg?branch=develop)](https://travis-ci.org/lenileiro/politico-api) 
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/politico-api?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2ba7d88ba0b45189d58fd361e33cea6)](https://www.codacy.com/app/lenileiro/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lenileiro/politico-api&amp;utm_campaign=Badge_Grade)

# Politico API's

## v1 endpoint

This project developer is to create a set of API endpoints defined in the API Endpoints Specification
section and use data structures to store data in memory 

Below are the Endpoints that have been created.

### Party Endpoints

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v1/parties | Create party| POST |
| api/v1/parties | Fetch all parties |GET|
| api/v1/parties/<int:party_id> |Fetch single party |GET|
| api/v1/parties/<int:party_id> |Delete party |DELETE|
| api/v1/parties/<int:party_id>/name|Edit party |PATCH|

### Office Endpoint

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v1/offices |Create office |POST|
| api/v1/offices |Fetch all offices |GET|
| api/v1/offices/<int:office_id> |Fetch single office |GET|

### Heroku Link

 Navigate to this [link](https://politico-v1-api.herokuapp.com/) to run the application on heroku


### TOOLS USED IN THE CHALLENGE

1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)
6. Testing Framework:[Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)

### Setup and Installation

1 Clone repo from github

        ```bash
            git clone https://github.com/lenileiro/politico-api.git

            cd politico-api

            git checkout develop branch
        ```

2 Create a virtual environment

        ```bash
            virtualenv venv

        ```
3 Activate the virtual environment

    
        ```bash
            source venv/bin/activate

        ```

4 Install project dependencies

         ```bash
            pip install -r requirements.txt

        ```

### Running Application

        ```bash
            source .env
            python run.py

        ```

### Running Tests

        ```bash
            coverage run --source=app -m pytest && coverage report

        ```

### author

[Anthony Leiro](https://github.com/lenileiro)