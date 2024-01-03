from django.db import models

# Create your models here.

class Song(models.Model):
    numero = models.CharField(max_length=500, blank=True, null=True)
    rrr = models.CharField(max_length=500, blank=True, null=True)  
    title_1 = models.CharField(max_length=500, blank=True, null=True)  
    title_2 = models.CharField(max_length=500, blank=True, null=True)  
    indirimbo = models.TextField(max_length=5000, blank=True, null=True)  
    categorie = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{str(self.id)} {self.title_1} {self.title_2}'







