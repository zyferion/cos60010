# cos60010
Code repository for COS60010 - Technical Enquiry Project.

Semester 1 2022

## Members
1. Mia
2. Erika
3. Natty
4. Andy

## Instructions

```bash
$ # Get the code
$ CLONE THIS REPO
$ CHANGE DIRECTORY TO PROJECT (directory where manage.py is stored)
$
$ # Virtualenv modules installation (Unix based systems)
$ python -m venv env 
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # py -m venv env 
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ python m pip install django
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port 
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
$
$ # Create admin account (super user)
$ py manage.py createsuperuser
$ 
$ # Access the admin page
$ # HERE: http://127.0.0.1:8000/admin

```
