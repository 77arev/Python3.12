from django.db import models


# Create your models here.
# ЭТО ДЛЯ БАЗ ДАННЫХ


class Skills(models.Model):
    title = models.CharField(max_length=100)  # текстовое поле с макс длиной символов 100
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills/images/')  # поле для изображений
    url = models.URLField(blank=True)  # ссылка на внешний ресурс

    def __str__(self):
        return self.title
