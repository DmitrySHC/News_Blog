from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    # blank mean that field can be ''
    created_at = models.DateTimeField('Date of publication', auto_now_add=True)
    updated_at = models.DateTimeField('Date of update', auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    # all photos will be saved in dir 'photos/'
    # and subdirs consonant with the year, month and day
    is_published = models.BooleanField(default=True)
