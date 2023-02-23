from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False, verbose_name="Статус")
    completion_date = models.DateField(auto_now=True, verbose_name="Выполнить до")


    def __str__(self):
        return f"{self.title} - {self.description} - {self.completion_date}"