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
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

<br />
4. And than you can run your server:
- using this command ```python manage.py runserver```

