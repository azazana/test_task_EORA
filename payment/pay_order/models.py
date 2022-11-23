from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return '{0:.f}'.format(self.price)


class Order(models.Model):
    email = models.EmailField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'item')


# class Discount(models.Model):
#     pass
#
#
# class Tax(models.Model):
#     pass
