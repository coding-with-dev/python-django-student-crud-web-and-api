from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.PositiveIntegerField()
    mobile = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)    

    def __str__(self):
        return self.name