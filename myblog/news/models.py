from django.db import models
from simple_history.models import HistoricalRecords


class Post(models.Model):
    '''Данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')
    history = HistoricalRecords()
    def __str__(self):
        return f'{self.title}, {self.author}, {self.date}, {self.description}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    '''Комментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.ip}, {self.post}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'