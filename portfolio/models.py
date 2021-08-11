from django.db import models

class Project(models.Model): # class to represent project
	title = models.CharField(max_length = 100)  # title of tha project
	description = models.CharField(max_length = 100)  # project details
	image = models.ImageField(upload_to = 'portfolio/images/') # project image
	url = models.URLField(blank = True) # url to redirect if we click project
	
	def __str__(self):
		return self.title