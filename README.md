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

There is a pre-made admin user already in the db:

```
$ user: admin
$ password: AdminPassword
```

Student details in dn:
```
$ user: student1
$ password: MondayGroup
```
*student can be ```student1```, ```student2```, ```student3```...

## Project Directory Structure

```
instatute/                      --- core project folder

static/                         --- contains static elements used across all pages of the web app (i.e. images/styles)
templates/                      --- contains html pages used across all pages of the web app (i.e. base html)

user/                           --- application directory for account management (register, log in/out)
quiz/                           --- application directory for quiz (quiz, questions, answers, results)
subjects/                       --- application directory for anything related to subjects (enrolments, leaderboards)

README.md
db.sqlite3
manage.py                       --- wrapper file for django-admin (allows you to run tasks)
```


## Useful Resources

1. Django Tutorial [https://www.w3schools.com/django/index.php]

