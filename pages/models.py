from django.db import models

class Products_listing(models.Model):
    product_title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    old_price = models.IntegerField(default=None, null=True,)
    product_img = models.ImageField(upload_to ='photos/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.product_title

