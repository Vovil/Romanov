from django.db import models

# Create your models here.
class task(models.Model):
	title = models.CharField('Имя', max_length=255)
	task = models.TextField('Описание')
	url = models.URLField('Ссылка')

	def __str__(self):
		return self.title