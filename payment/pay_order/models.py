from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return '{0:.f}'.format(self.price)
