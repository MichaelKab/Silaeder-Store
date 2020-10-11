from django.db import models
from .customuser import CustomUser


class Product(models.Model):
    name_product = models.CharField(max_length=60)
    description_product = models.CharField(max_length=500)
    quantity = models.SmallIntegerField(default=0)
    buyers = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return "Название:{} Описание:{}  Кол-во:{}".format(self.name_product, self.description_product, self.quantity)
