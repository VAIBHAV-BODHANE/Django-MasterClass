from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://fitmirchi.com/admin/assets/images/image_not_available.png")

    def __str__(self):
        return self.item_name