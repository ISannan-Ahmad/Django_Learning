from django.db import models

# Create your models here.
class Item(models.Model):

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.item_name
    