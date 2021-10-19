# News blog

---
#### (under development: functions "Добавить новость" and "Read more" on the main page do not work yet)
It's just a news blog.

![img.png](img.png)

Instruction for use:

1. Create a database (blog use mysql) and specify it in a variable "DATABASES" (path: News_Blog/News_Blog/settings.py):
> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_news',
        'USER': 'root',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost'
    }
}
 
Enter the database NAME, USERNAME and PASSWORD (from MySQL workbench).

2. Make migrations (all commands are entered in the directory with "manage.py"): 
>python manage.py migrate
> 
>python manage.py makemigrations

3. Create a superuser:
> python manage.py createsuperuser
 
Enter Username, Email address and password.

4. Then you can start the test server:
>python manage.py runserver

Use your username and password to enter: http://127.0.0.1:8000/admin/

And now you can add news, and they will be represented on the main page: http://127.0.0.1:8000
![img_1.png](img_1.png)




