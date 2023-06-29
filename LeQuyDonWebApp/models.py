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
class DaHocHetLop5(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Truong(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class TruongVaQuan(models.Model):
    truong = models.ForeignKey(Truong, on_delete=models.CASCADE)
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)
class DangKyHoc(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name
class DonTuyenSinh(models.Model):
    ten = models.CharField(max_length=100, unique=False)
    sdt = models.CharField(max_length=100,null=False)
    hokhau = models.CharField(max_length=100)
    choDK = models.CharField(max_length=100)
    cccd = models.IntegerField()
    is_parent = models.CharField(max_length=100)
    trinhdo = models.ForeignKey(DaHocHetLop5, on_delete=models.CASCADE)
    truongtieuhoc = models.CharField(max_length=100)
    tenhs = models.CharField(max_length=100)
    ngaysinh = models.DateField(auto_now=True)
    gioitinh = models.CharField(max_length=100)
    dantoc = models.CharField(max_length=100)
    tongiao = models.CharField(max_length=100)
    noisinh = models.CharField(max_length=100)
    madinhdanh = models.CharField(max_length=100)
    diachi = models.CharField(max_length=100, unique=False)
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)
    phuong = models.CharField(max_length=100)
    diachithuongtru = models.CharField(max_length=100)
    quanthuongtru = models.CharField(max_length=100)
    phuongthuongtru = models.CharField(max_length=100)
    dienchinhsach = models.CharField(max_length=100, null=True)
    suckhoe = models.CharField(max_length=100)
    tiengviet5 = models.FloatField(max_length=100)
    toan5 = models.FloatField(max_length=100)
    tongdiem = models.FloatField()
    chungchita = models.CharField(max_length=100)
    cambridge = models.IntegerField(null=True)
    toefl = models.IntegerField(null=True)
    pearson = models.FloatField(null=True)
    hocba = models.CharField(max_length=100)
    boi = models.CharField(max_length=100)
    nangkhieu = models.CharField(max_length=100,null=True)
    tdtt = models.CharField(max_length=100, null=True)
    tntp = models.CharField(max_length=100, null=True)
    tencha = models.CharField(max_length=100)
    namsinhcha = models.IntegerField()
    nghenghiep = models.CharField(max_length=100)
    chucvu = models.CharField(max_length=100)
    noicongtac = models.CharField(max_length=100)
    sdtcha = models.IntegerField()
    tenme = models.CharField(max_length=100)
    namsinhme = models.IntegerField()
    nghenghiepme = models.CharField(max_length=100)
    chucvume = models.CharField(max_length=100)
    noicongtacme = models.CharField(max_length=100)
    sdtme = models.CharField(max_length=100)
    chonlop = models.ForeignKey(DangKyHoc, on_delete=models.CASCADE)




