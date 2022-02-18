1. django-admin startproject
2. python3 manage.py runserver
3. python3 manage.py migrate
4. python3 manage.py makemigrations
# then 3 again to make tables in the database
5. python3 manage.py createsuperuser
# Models have default id increament with each row in the database


# to see db in admin dashboard in base/admin.py
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

# in settings to connect the static files with our project 
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# to go to the past page
<a href="{{ request.META.HTTP_REFERER }}"></a>
 