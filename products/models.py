from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_describe = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://schulershoes-magento.s3.amazonaws.com/pub/media/catalog/product/placeholder/default/PLACEHOLDER.jpg")
