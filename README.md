# Virtual Environment + DJango Lesson
## [Dev.f GDL](https://www.devf.mx/guadalajara) - Cinta Negra - Batch 1
=================

**Installation:**
-----------------

```
#> pip install virtualenv  --> Install virtualenv
#> virtualenv <environment-name>
```

To run the Environment is:

- **Mac/Unix**
source bin\activate

- **Win**
Scripts/activate.bat

```
(Environment)>   --> This is how the Terminal should looks like when activated, run the commands inside this 'context'

(Environment)> pip install django

(Environment)> mkdir <django-app>

(Environment)> django-admin startproject <django-project>  

(Environment)> py manage.py runserver   -> run server

(Environment)> py manage.py startapp <django-app>  -> Create an App (Model?)

(Environment)> py manage.py shell -> Opens the Interactive Shell

```

## DJango Project Environment
-------------------------

settings.py
urls.py
wsgi.py


## Models + Migrations
---------------------

- Make sure you have your DB Connection parameters for your DBMS, Also be sure you have your drivers installed (mysqlclient for mysql)
- Create you model into the app/models.py file
- Append your model into settings.py into INSTALLED_APPS object/array
- Once we have the model, run:
```
(Environment)> py manage.py makemigrations
```
- Once we have the migrations files, we can run it:
```
(Environment)> py manage.py migrate   
```
You can create a model into your Database using the Interactive Shell
```
(Environment)> py manage.py shell
(Interactive Shell)> from <app-name> import *
(Interactive Shell)> <variable> = <app-name>.objects.create({Params}...)

