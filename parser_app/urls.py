from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
   path('' , show_form) ,
   path('page/' , create),
   path('page/<int:id>/' , get_by_id)
]
