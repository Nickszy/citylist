from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=100, primary_key=True)
    # ename = models.CharField()
    des = models.TextField()
    tags = models.TextField()

    class Meta:
        db_table = 'city_des'

# class City_data(models.Model):
#     class META:
#         db_table = 'city_data'

#     medical = models.FloatField()

#     dict()

