from django.contrib import admin
from django.urls import path , include
from core import views
urlpatterns = [    
    path( "", views.index , name="index"),
    path( "add_student", views.add_Student , name="add_Student"),
    
]
