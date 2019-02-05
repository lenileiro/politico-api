# Badges

[![Build Status](https://api.travis-ci.org/lenileiro/politico-api.svg?branch=develop)](https://travis-ci.org/lenileiro/politico-api) 
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/politico-api?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2ba7d88ba0b45189d58fd361e33cea6)](https://www.codacy.com/app/lenileiro/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lenileiro/politico-api&amp;utm_campaign=Badge_Grade)

## Politico-api

Backend service where admin can:

- Create a political party.
- Get all political parties.
- Get a specific political party.
- Edit a specific political party.
- Delete a particular party.
- Create a political office.
- Get all political offices.
- Get a specific political office.

## Prerequisites

- Python 3.6.7
- Postman


## Installation

1. Clone this repository :

    ```bash
    #!/bin/bash
    $ git clone https://github.com/lenileiro/politico-api.git
    ```

2. CD into the project folder on your machine

    ```bash
    #!/bin/bash
    $ cd politico-api
    $ pip install virtualenv
    ```

3. Create a virtual environment

   ```bash
    #!/bin/bash
    $ virtualenv venv
    ```

4. Activate the virtual environment

    ```bash
    #!/bin/bash
    $ source venv/bin/activate
    ```

5. Install the dependencies from the requirements file

    ```bash
    #!/bin/bash
    $ pip install -r requirements.txt
    ```

6. Run the application

    ```bash
    #!/bin/bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    flask run
    ```
