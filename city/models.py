from django.db import models

# Create your models here.
class City(models.Model):
    id = models.IntegerField()
    city = models.CharField(max_length=100, primary_key=True)
    # ename = models.CharField()
    # uprovince = ('安徽省','浙江省','江苏省','')
    province = models.CharField(max_length=20)
    tags = models.TextField()
    des = models.TextField()
    address = models.CharField(max_length=20)
    click_num = models.IntegerField(default=0)
    lng = models.FloatField()
    lat = models.FloatField()

    class Meta:
        db_table = 'city_des'


class Count(models.Model):
    class Meta:
        db_table = 'count_city'
    city = models.CharField(max_length=100, primary_key=True)
    count_city_click_num= models.IntegerField()

class City_click(models.Model):
    class Meta:
        db_table = 'city_click'
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    time = models.DateTimeField()
    city = models.CharField(max_length=30)
    city_id = models.IntegerField()
    ip = models.CharField(max_length=30)


# class City_data(models.Model):
#     class META:
#         db_table = 'city_data'

#     medical = models.FloatField()

#     dict()

