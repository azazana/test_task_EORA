from django.db import models


class Tax(models.Model):
    percent = models.IntegerField(default=0)

    def __str__(self):
        return str(self.percent)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_price(self):
        return '{0:.f}'.format(self.price)


class Discount(models.Model):
    percent = models.IntegerField(default=0)

    def __str__(self):
        return str(self.percent)


class Order(models.Model):
    email = models.EmailField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'item')
