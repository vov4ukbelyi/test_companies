# test_companies

### Installation and setup
After cloning this repository to your local folder, you can use virtualenv for testing.<br />
1. Run command ```virtualenv venv``` in folder where requirements.txt is situated. You create folder with name "venv".
2. Then use command ```venv/bin/activate``` to go in virualenv and install all requirements using ```sudo pip install -r requirements.txt```. <br />Use ```python manage.py collectstatic``` for collect static files. <br />
3. Than you need to configure you database:<br />
- ```sudo -u postgres psql```
- ```create user companyuser;```
- ```create database companydb owner companyuser;```
- ```alter user companyuser with encrypted password 'mypassword';```
- ```\q
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- ```python manage.py createsuperuser```

<br />
4. And than you can run your server:<br />
- using this command ```python manage.py runserver```

### Heroku Deploy and local settings
### Deploy
After cloning this repository to your local folder, you must configure you database so do Step 3 in Installatuion and setup.
1. Run command ```heroku create``` in folder where requirements.txt.
2. Use ```git push heroku master``` for push app in Heroku.
3. Command ```heroku run python manage.py migrate``` migrate db in server Heroku.
<br />
4. Then you can run your server ```heroku ps:scale web=1```. And open them in browser ```heroku open```.<br />

### Local Heroku
After cloning this repository to your local folder, you must configure you database so do Step 3 in Installatuion and setup.
1. Run command ```virtualenv venv``` in folder where requirements.txt.
2. Then use command ```venv/bin/activate``` to go in virualenv and install all requirements using ```sudo pip install -r requirements.txt```. <br />Use ```python manage.py collectstatic``` for collect static files. <br />
3. Command ```export DATABASE_URL=postgres:///$(whoami)``` tells Postgres to connect locally to the database matching your user account name(which is set up as part of installation).
4. Then you can run your Heroku local server heroku ```local web```.


### Errors ###
If you have error ```no module named mptt``` please download <a href="https://pypi.python.org/packages/d6/b9/918d3e5098af86bedc30ed1827d2223f03fd7ca0454a2d666fd39b00a1ee/django-mptt-0.8.7.tar.gz#md5=b2f40f07f3cb81b706808ce5ebb17bc0">Packeg</a>, unpack him and do command ```python setup.py install```.
