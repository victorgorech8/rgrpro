from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

import sys
sys.path.append('C:/Users/victo/rgrpro')
from bottest import send_telegram

User = get_user_model()


class SQLq(models.Model):
    """
    Модель постов для сайта
    """    

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'), 
        ('draft', 'Черновик')
    )

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    
    full_description = models.TextField(verbose_name='Полное описание')
   
    
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    
    fixed = models.BooleanField(verbose_name='Зафиксировано', default=True)
    
        
    class Meta:
        db_table = 'app_articles'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create'])]
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        
        return self.title
    
    def save(self, *args, **kwargs):
        super(SQLq, self).save(*args, **kwargs)
        send_telegram(str(self.full_description))