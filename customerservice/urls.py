from django.conf.urls import url
from . import views

app_name = 'customerservice'

urlpatterns = [
    url(r'^customer/$', views.customer_create, name='cust_create')
]