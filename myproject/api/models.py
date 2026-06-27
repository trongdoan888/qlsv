from django.db import models

class LopHoc(models.Model):
    name = models.CharField(max_length=50, unique=True)

# Create your models here.
class sinhvien(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    id = models.CharField(max_length=20, primary_key=True)
    lop = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='student')

    # class_rooms = models.ManyToManyField(LopHoc, related_name="students")

    def __str__(self):
        return self.name
    
class giangvien(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    id = models.CharField(max_length=20, primary_key=True)
    khoa = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='teacher')
    def __str__(self):
        return self.name
    
class account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Lưu mật khẩu đã được hash
    role = models.CharField(max_length=20)  # 'teacher', 'student'
    id = models.CharField(max_length=20, primary_key=True)  # Mã sinh viên hoặc giảng viên

    def __str__(self):
        return self.username
    

