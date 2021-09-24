from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=200)
    content = models.TextField(verbose_name='Контент', blank=True)
    # blank mean that field can be ''
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d')
    # all photos will be saved in dir 'photos/'
    # and subdirs consonant with the year, month and day
    is_published = models.BooleanField(verbose_name='Новость опубликована', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']
