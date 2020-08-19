#######################
Wagtail Website Builder
#######################

Build websites using Wagtail CMS.

Development
###########

* Create database
    ```python3
    CREATE DATABASE wwb;
    CREATE USER wwb WITH PASSWORD 'password';
    ALTER ROLE wwb SET client_encoding TO 'utf8';
    ALTER ROLE wwb SET default_transaction_isolation TO 'read committed';
    ALTER ROLE wwb SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE wwb TO wwb; 
    \q
    ```

* Migrate database using `python manage.py migrate`
* Create super user `python manage.py createsuperuser`
* Run development server `python manage.py runserver`