from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'wishlist'

urlpatterns = [

    url(r'^wish/$', views.WishListView.as_view(), name='wishlistitems'),
    path("addwish/<int:pk>/", views.AddWishItem, name='addwishlist'),
    path("deletewish/<int:pk>/",views.Deletewishlistitem.as_view(),name="deletewishitem"),
]