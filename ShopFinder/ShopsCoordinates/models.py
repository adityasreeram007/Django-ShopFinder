from django.db import models

class Shop(models.Model):
   shopId=models.IntegerField(unique=True)
   shopName=models.CharField(max_length=40) 
   latitude=models.FloatField()
   longtitude=models.FloatField()
   class Meta:
      db_table="shops"