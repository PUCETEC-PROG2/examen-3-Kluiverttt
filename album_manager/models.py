from django.db import models

# Create your models here.
class Artist(models.Model):    
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portada/')

    def __str__(self):
        return self.title