
from django.urls import path,include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    
    path(r'temp',csrf_exempt(views.temp),name="temp"),
    path(r'deleteShop',csrf_exempt(views.deleteShop),name="delete"),
    path(r'fetchShop',csrf_exempt(views.fetchShop),name='fetch'),
    path(r'addShop',csrf_exempt(views.addShop),name='add'),
    path(r'updateShop',csrf_exempt(views.updateShop),name='update'),
    path(r'findShop',csrf_exempt(views.getNearestToRadius),name="findShop")

]