# from .Model import Shop

# data=[[1,"ibaco","12.8","7.8"],[2,"apples","12.8","6.8"],[3,"acko","12","7.8"],[4,"cakebakeo","12.8","8.9"],[5,"ib","11.8","9.8"]]
# for d in data:
#    s=Shop(shopId=d[0],shopName=d[1],latitude=d[2],longtitude=d[3])
#    s.save()
from django.core import serializers
print(serializers.serialize("json",[False]))