from django.db import models

# Creating models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.IntegerField()

    def __str__(self):
        return self.name
    
