# restapis-django-basics


    1- vagrant up
    2- vagrant ssh (login to vagrant)
    3- python -m venv ~/env (create virtual env)
    source ~/env/bin/activate
    deactviate
    
    Activate irtual env and pip install command V
    pip  freeze>requirements.txt


    docker-compose run app sh -c  "python manage.py test && flake8"
    heroku auth:token
    travis encrypt {heroku tokem} --add deploy.api_key --pro  heroku 
    heroku config:set DISABLE_COLLECTSTATIC=1 --app restapis-django-basics
    heroku run python manage.py createsuperuser --app restapis-django-basics
    heroku addons:create heroku-postgresql  --app restapis-django-basics


