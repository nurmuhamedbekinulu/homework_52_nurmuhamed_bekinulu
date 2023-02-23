from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")


    def __str__(self):
        return f"{self.author} - {self.title}"


class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(
        to='webapp.Article',
        verbose_name='Статья',
        null=False,
        blank=False,
        related_name='comments',
        on_delete=models.RESTRICT
        )
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")


    def __str__(self):
        return f"{self.text} - {self.created_at}"
