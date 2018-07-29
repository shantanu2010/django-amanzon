from django.db import models

# Create your models here.


class Customerservice(models.Model):

    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_no=models.IntegerField()
    order_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250,default=None)
    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Customer Service {}'.format(self.id)
