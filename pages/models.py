from django.db import models

class Products_listing(models.Model):
    product_title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to ='photos/%Y/%m/%d/',blank=True)

