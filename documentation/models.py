from django.db import models

# Create your models here.

class Documentation(models.Model):
    
    code = models.CharField(max_length=10, primary_key=True)

    url = models.URLField()

    description = models.TextField()

    width = models.IntegerField()
