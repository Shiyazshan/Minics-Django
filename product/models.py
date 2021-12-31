from django.db import models
from django.db.models.expressions import F
from django.db.models.fields.related import ForeignKey

class Product(models.Model):
    image = models.ImageField(upload_to='product',blank=True,null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_rating = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.product.title


class Cart(models.Model):
    items = models.ManyToManyField(CartItem,null=True,blank=True)
    products = models.ManyToManyField(Product, null=True,blank=True)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)
        