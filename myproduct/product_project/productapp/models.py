from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=250)
    bdesc=models.TextField()
    byear=models.IntegerField()
    bimg=models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.bname