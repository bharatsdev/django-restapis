[![Build Status](https://travis-ci.com/everythingisdata/restapis-django-basics.svg?branch=main)](https://travis-ci.com/everythingisdata/restapis-django-basics)

# restapis-django-basics
Basic integraiton for Django and DB.

Tech Stack :
       
        Python 3
        Django
        Django Rest
        Docker
        Docker-compose 
        PostgreSQL
        Swagger
        
 ## Getting Start
    
    START APPLICAITON ON LOCAL MACHINE 
    
    >docker-compose up --build
    > docker-compose run app sh -c  "python manage.py test && flake8"

## Heroku Setup 
create an account on heroku and create a application 

    heroku auth:token
    travis encrypt {heroku tokem} --add deploy.api_key --pro  heroku 
    heroku config:set DISABLE_COLLECTSTATIC=1 --app restapis-django-basics
    heroku run python manage.py createsuperuser --app restapis-django-basics


