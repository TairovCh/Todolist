from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Аватар')
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Ссылка')
    about_me = models.TextField(max_length=3000, null=True, blank=True, verbose_name="О себе")

    def __str__(self):
        return f"{self.user.username} 's Profile"

    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'