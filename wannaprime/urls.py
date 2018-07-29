from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'wannaprime'

urlpatterns = [

    path('', views.wanna_prime, name='sell_prime'),
]