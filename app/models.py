from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
	like = models.ManyToManyField(User,default=None,blank=True)
	customer = models.CharField(max_length=200)

