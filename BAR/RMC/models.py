from django.db import models
# Create your models here.


class Events(models.Model):
	name=models.CharField(max_length=100)
	img =models.ImageField(upload_to='pics')
	des =models.TextField(max_length=500)

class Gallary(models.Model):
	img =models.ImageField(upload_to='pics')
	des =models.TextField(max_length=500)



	