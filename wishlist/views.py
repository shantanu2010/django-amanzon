from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from wishlist.models import Wishlist
from shop.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

class WishListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    model = Wishlist
    context_object_name = 'object'
    template_name = "wishlist/wishlist_list.html"

    def get_queryset(self):
        user = self.request.user
        return Wishlist.objects.filter(user_id=user.id)

    def get_context_data(self, **kwargs):
        context = super(WishListView, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


def AddWishItem(request, pk):

    if request.user.is_authenticated:
        user = request.user
        item = Product.objects.get(id=pk)

        temp = Wishlist.objects.all().filter(user_id=user.id)

        for obj in temp:
            if obj.product == item:
                break
        else:
            wishlistitem = Wishlist(user_id=user.id, price=item.price, image=item.image,product = item)
            wishlistitem.save()
        return redirect('shop:product_list')

    return redirect('shop:login')


class Deletewishlistitem(LoginRequiredMixin,DeleteView):

    model = Wishlist
    template_name = 'wishlist/deletewishlist.html'
    success_url = reverse_lazy('wishlist:wishlistitems')

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        check_user = Wishlist.objects.get(pk=pk).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('wishlist:wishlistitems')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('wishlist:wishlistitems')
            return True