# Screened-Movie-Blog

This a blog for movie reviews.

## Table of Contents

- [Running](#running-locally)
  
## Running locally

1. install python
   download from the official python [download](https://www.python.org/downloads/) page
   
- install virtualenv `pip install virtualenv`
- install django `pip install django`

2. clone the repository and move into the repository

   ```bash

   git clone https://github.com/Jozz77/Screened-Movie-Blog.git

   ```

3. create the virtual environment if you haven't created it

   ```bash

    python -m venv env

   ```

4. activating the virtual environment

   windows:
   `.\env\Scripts\activate`

   macOs:
   `source env/bin/activate`

5. install the requirements

   ```bash

   pip install -r requirements.txt

   ```

6. make migrations to the database

   ```bash

    python manage.py makemigrations

   ```

7. migrate to the database

   ```bash

    python manage.py migrate

   ```

8. run

   ```bash

    python manage.py runserver

   ```
