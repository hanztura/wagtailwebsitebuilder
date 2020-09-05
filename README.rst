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
  
Oscar - eCommerce
#################

* Populate countries `python manage.py oscar_populate_countries`


RemovedInWagtail211Warning
##########################

RemovedInWagtail211Warning: wagtail.core.middleware.SiteMiddleware and the use of request.site is deprecated. Please update your code to use Site.find_for_request(request) in place of request.site, and remove wagtail.core.middleware.SiteMiddleware from MIDDLEWARES
