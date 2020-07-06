from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    vin = models.CharField(verbose_name='Вин', db_index=True, unique=True, max_length=64)
    head = models.CharField(verbose_name='Заголовок', max_length=64)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    body = models.CharField(verbose_name='Содержание', max_length=256)
    TOPICS = (
        (1, 'Наука'),
        (2, 'Природа'),
        (3, 'Технологии'),
        (4, 'Языки'),
        (5, 'Люди'),
    )
    topic = models.IntegerField(verbose_name='Тема', choices=TOPICS)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
