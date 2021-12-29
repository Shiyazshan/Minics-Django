from django.db import models
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

class Cart(models.Model):
    product = models.ForeignKey("product.Cart",on_delete=models.CASCADE)

    def __str__(self):
        return self.product
        