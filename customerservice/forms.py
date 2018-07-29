from django import forms
from .models import Customerservice


class CustomerserviceCreateForm(forms.ModelForm):
    class Meta:
        model = Customerservice
        fields = ['name','email', 'phone_no','order_id','description']