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
        db_table='user_login'