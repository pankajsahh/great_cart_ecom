
from tabnanny import verbose
from django.db import models


class Catagory(models.Model):
    Catagory_name = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)
    class Meta:
        verbose_name='catagory'
        verbose_name_plural='catagories'
        
    def __str__(self):
        return self.Catagory_name