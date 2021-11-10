# Generated by Django 3.2.8 on 2021-10-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('task', models.TextField(verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
        ),
    ]
