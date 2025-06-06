from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creator = models.CharField(max_length=100)
    image = models.TextField()
    link = models.TextField()
    
    def __str__(self):
        return self.title