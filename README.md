# News blog

---
#### (under development: functions "Добавить новость" and "Read more" on the main page do not work yet)

It's just a news blog with categories.

![img.png](img.png)

### Instruction for use without docker:

1. Create empty database:
>mysql create database <db_name>

Enter the database NAME, USER and PASSWORD (from MySQL Server) in variable "DATABASES":
> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<db_name>',
        'USER': '<user_name>',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost'
    }
}

2. Make migrations (all commands are entered in the directory with "manage.py"): 
>python manage.py migrate


3. Create a superuser:
> python manage.py createsuperuser
 
Enter Username, Email address and password.

4. Then you can start the test server:
>python manage.py runserver

Use your superuser username and password to enter: http://127.0.0.1:8000/admin/

And now you can add news and categories, and they will be represented on the main page: http://127.0.0.1:8000
![img_1.png](img_1.png)


### Instruction for use with docker:

1. Create the image:

> docker-compose build

2. Create superuser:

> docker-compose run blog python manage.py createsuperuser

Enter Username, Email address and password.

3. Run the containers:

> docker-compose up

Use your superuser username and password to enter: http://127.0.0.1:8000/admin/

And now you can add news and categories, and they will be represented on the main page: http://127.0.0.1:8000