from django.db import models

# Create your models here.
class Geeks(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Название курса",
    )

    content = models.TextField(
        verbose_name="Описание курса",
    )