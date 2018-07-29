from django.shortcuts import render
from .models import Customerservice
from .forms import CustomerserviceCreateForm


def customer_create(request):
    cart = Customerservice(request)
    if request.method == 'POST':
        form = CustomerserviceCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            return render(request, 'customerservice/detail.html', {'customer': order})
    else:
        form = CustomerserviceCreateForm()
    return render(request, 'customerservice/create.html', {'form': form})