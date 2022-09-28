# Screened-Movie-Blog

This a blog for movie reviews.

## URLS

- login page: localhost/user/login
- signup page: localhost/user/signup
- reset password page: localhost/user/password_reset/
- password reset confirmation page i.e. The reset link has been sent to your email: localhost/user/password_reset_confirm/
- password reset complete: localhost/user/password_reset_complete/



## Table of Contents

- [Running](#running-locally)
  
## Running locally for the first time

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

6. run

   ```bash

    python manage.py runserver

   ```
   
   
## Running after the first time

1. activate the environment

  windows:
   `.\env\Scripts\activate`

   macOs:
   `source env/bin/activate`
   
 2. run the server

```bash

python manage.py runserver

```
