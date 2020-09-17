from django.db import models
# Create your models here.
class UserData(models.Model):
    user_id = models.IntegerField(default=0, unique= True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    midle_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.user_id, self.username, self.first_name, self.midle_name, self.last_name, self.score)


class Transaction(models.Model):
    id_user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cash = models.IntegerField(default=0)
    date = models.DateTimeField()
    def __str__(self):
        return "ID:{}  Кол-во:{}  Дата:{}".format(self.id_user.user_id, self.cash, self.date)


class Product(models.Model):
    name_product = models.CharField(max_length=60)
    description_product = models.CharField(max_length=500)
    quantity = models.SmallIntegerField(default=0)
    buyers = models.ManyToManyField(UserData)
    def __str__(self):
        return '''Название:{}Описание:{}  Кол-во:{}'''.format(self.name_product, self.description_product, self.quantity)