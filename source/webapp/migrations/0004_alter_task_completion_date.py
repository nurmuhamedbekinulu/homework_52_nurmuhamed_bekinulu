# Generated by Django 4.1.6 on 2023-02-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_task_remove_comment_article_delete_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_date',
            field=models.DateField(blank=True, null=True, verbose_name='Выполнить до'),
        ),
    ]