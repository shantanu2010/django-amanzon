from django import forms
from shop.models import *
import itertools
from django.utils.text import slugify

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['id', 'owner_id']
        fields = (
            'category',
            'name',
            'description',
            'price',
            'available',
            'stock',
            'image'
        )

    def save(self,commit):
        instance = super(AddProductForm, self).save(commit=False)

        temp = instance.name
        temp = temp.lower()
        temp = temp.split()
        res = ""
        k = ""
        for i in temp:
            p = [c for c in i if c.isalpha()]
            k = ''.join(p)
            res += "_" + k
            k = ""

        instance.slug = res

        return instance



class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['id', 'owner_id']
        fields = (
            'name',
            'description',
            'price',
            'available',
            'stock',
            'image'
        )

    def save(self):
        instance = super(AddProductForm, self).save(commit=False)

        max_length = Product._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Product.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()

        return instance