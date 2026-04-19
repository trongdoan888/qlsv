from django.db import models

# Create your models here.
class sinhvien(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    id = models.CharField(max_length=20, primary_key=True)
    lop = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class giangvien(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    id = models.CharField(max_length=20, primary_key=True)
    khoa = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

