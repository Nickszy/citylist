from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=100, primary_key=True)
    # ename = models.CharField()
    # uprovince = ('安徽省','浙江省','江苏省','')
    province = models.CharField(max_length=20)
    tags = models.TextField()
    des = models.TextField()
    address = models.CharField(max_length=20)
    class Meta:
        db_table = 'city_des'

# class City_data(models.Model):
#     class META:
#         db_table = 'city_data'

#     medical = models.FloatField()

#     dict()

