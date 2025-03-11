from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('dress/',dress,name='dress'),
     path('perfume/',perfume,name='perfume'),

]