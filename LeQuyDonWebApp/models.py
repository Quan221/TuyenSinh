from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class Quan(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name

class Phuong(models.Model):
    name = models.CharField(max_length=100, unique=True)




    def __str__(self):
        return self.name

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m/', null=True)



class QuanvaPhuong(models.Model):
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)
    phuong = models.ForeignKey(Phuong, on_delete=models.CASCADE)
class Products(models.Model):
    name = models.CharField(max_length=100, unique=False)
    sdt = models.IntegerField(null=False)
    diachi = models.CharField(max_length=100, unique=False)
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)
    phuong = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    cccd = models.IntegerField()
    is_parent = models.CharField(max_length=100)



