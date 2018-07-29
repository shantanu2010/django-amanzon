from django.conf.urls import url
from . import views
from django.urls import path
from login_signup.views.auth import *
app_name = 'shop'

urlpatterns = [

    path('logout/', logout_view, name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),


    path('', views.product_list1, name='product_list'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('addproduct/<int:pk>/', views.CreateProductView.as_view(), name='add_product'),
    path('api/search/',views.SearchUser,name='search'),



]