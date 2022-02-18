1. django-admin startproject
2. python3 manage.py runserver
3. python3 manage.py migrate
4. python3 manage.py makemigrations
# then 3 again to make tables in the database
5. python3 manage.py createsuperuser
# Models have default id increament with each row in the database

# in settings to connect the static files with our project 
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
 