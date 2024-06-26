from django.db import models
from pages.models import Products_listing

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)


class CartItem(models.Model):
    product = models.ForeignKey(Products_listing, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.product_price * self.quantity

    def __unicode__(self):
        return self.product
