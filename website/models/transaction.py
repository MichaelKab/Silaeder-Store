from django.db import models
from .customuser import CustomUser


class Transaction(models.Model):
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cash = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return "ID:{}  Кол-во:{}  Дата:{}".format(self.id_user.id, self.cash, self.date)
