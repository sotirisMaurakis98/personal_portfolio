from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 40)
	date = models.DateField(auto_now_add = True)
	description = models.TextField(max_length = 100)

