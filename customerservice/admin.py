from django.contrib import admin
from .models import Customerservice
# Register your models here.


class CustomerserviceAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','phone_no','order_id', 'created','description']
    list_filter = ['created']


admin.site.register(Customerservice, CustomerserviceAdmin)