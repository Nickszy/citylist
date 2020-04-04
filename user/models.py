from django.db import models

# Create your models here.
class User(models.Model):
    ugender = (
        ('male', "男"),
        ('female', "女"),
    )
    uname = models.CharField(max_length=128)
    upass = models.CharField(max_length=256)
    uemail = models.EmailField()
    usex = models.CharField(max_length=6,choices=ugender)
    class Meta():
        db_table='user'

class User_login(models.Model):
    class Meta():
        db_table='user_status'
    ip = models.CharField(max_length=20)
    user_id = models.IntegerField()
    time = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
