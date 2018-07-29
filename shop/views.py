from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django import forms
from shop.forms.product_views import *
from cart.forms import CartAddProductForm
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from datetime import datetime as dt
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework import serializers
from PIL import Image
from random import randint
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_list1(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    #frequentBuying = []

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    count = Product.objects.count()

    #for i in range(0,7):
    #    random_object = Product.objects.all()[randint(0, count - 1)]
    #    frequentBuying.append(random_object)

    frequentBuying = Product.objects.all()
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'frequents':frequentBuying
    }
    return render(request, 'shop/product/all.html', context)

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


class CreateProductView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'shop/add.html'
    login_url = '/login'

    def post(self, request, *args, **kwargs):

        form = AddProductForm(request.POST,request.FILES)
        i=0
        s=""
        t = UserProfile.objects.get(user_id=request.user.id)
        if form.is_valid() and t.status_flag == 1:
            cc_object = form.save(commit=False)
            cc_object.owner_id = request.user.id
            #i = cc_object.id
            #s = cc_object.slug
            cc_object.save()
        #return render(request,'shop:product_details',context={"id":i,"slug":s})
            return HttpResponseRedirect(cc_object.get_absolute_url())
        return HttpResponseRedirect(reverse('shop:login'))

class ProductdataSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


def SearchUser(request):

    if request.method == "GET":
        products = Product.objects.all().filter(name__icontains=request.GET['query'])
        #products = Product.objects.all().filter(name__icontains=id)
        serializers = ProductdataSerializer(products, many=True)
        return JsonResponse(serializers.data, safe=False)