from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Shop
from django.core import serializers
import json
from .helper import findInRadius
# Create your views here.


def temp(request):
   findInRadius(6,11.8,9.8,Shop.objects.all())
   return HttpResponse(True)

def getNearestToRadius(request):
   if request.method == "POST":
      print(request.POST)
      if all(key in request.POST for key in ["r","lat","lon"]):
         return HttpResponse(serializers.serialize('json',findInRadius(float(request.POST["r"]),float(request.POST["lat"]),float(request.POST["lon"]),Shop.objects.all())),content_type='application/json')
   return HttpResponse(False)


   
def deleteShop(request):
   if request.method=="POST":
      if "id" in request.POST:
         print(request.POST['id'])
         s=Shop.objects.filter(shopId=int(request.POST['id']))
         print(s)
         if s!=None:
            s[0].delete()
            return HttpResponse(True)
      return HttpResponse(False)

def fetchShop(request):
   if request.method=="POST":
      # print(request.POST['id'])
      if "id" in request.POST:
         # return Shop.objects.get(shopId=int(request.POST['id']))
         # return json.dumps(Shop.objects.get(shopId=int(request.POST['id'])))
         print(Shop.objects.filter(shopId=int(request.POST['id'])))
         return HttpResponse(serializers.serialize('json', Shop.objects.filter(shopId=int(request.POST['id']))), content_type='application/json')
      return HttpResponse(serializers.serialize('json', Shop.objects.all()), content_type='application/json') 

def addShop(request):
   if request.method=="POST":
      if all(key in request.POST for key in ["id","name","latitude","longtitude"]):
         d=[request.POST["id"],request.POST["name"],request.POST["latitude"],request.POST["longtitude"]]
         s=Shop(shopId=d[0],shopName=d[1],latitude=d[2],longtitude=d[3])
         s.save()
         return HttpResponse(True)
   return HttpResponse(False)

def updateShop(request):
   if request.method=="POST":
      s=Shop.objects.filter(shopId=int(request.POST['id']))
      print(s)
      if s!=None:
         s[0].delete()
      else:
         return HttpResponse(False)
      if all(key in request.POST for key in ["id","name","latitude","longtitude"]):
         d=[request.POST("id"),request.POST("name"),request.POST("latitude"),request.POST("longtitude")]
         s=Shop(shopId=d[0],shopName=d[1],latitude=d[2],longtitude=d[3])
         s.save()
         return HttpResponse(True)
      else:
         return HttpResponse(False)