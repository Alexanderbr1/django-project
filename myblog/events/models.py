from django.db import models

class Sport(models.Model):
    '''Вид спорта'''
    name = models.CharField('Вид спорта', max_length=100)

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    '''Данные о посте'''
    title = models.CharField('Название мероприятия', max_length=200)
    sports = models.ManyToManyField('Sport', through='Participation')
    description = models.TextField('Описание мероприятия')
    location = models.CharField('Место проведения', max_length=200)
    date = models.DateField('Дата проведения')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.location}, {self.date}, {self.sports}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sport} - {self.event}"

    class Meta:
        verbose_name = 'Событие - виды спорта'
        verbose_name_plural = 'Событие - виды спорта'

class EventComments(models.Model):
    '''Комментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    event = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.event}, {self.text_comments}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class EventLikes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Event, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip}, {self.pos}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


