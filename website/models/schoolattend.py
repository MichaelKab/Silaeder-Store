from django.db import models
from .customuser import CustomUser


class SchoolAttend(models.Model):
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    required_days = models.CharField(max_length=16)
    time_start = models.SmallIntegerField(default=0)
    exception_days = models.CharField(max_length=120)

    def __str__(self):
        return "ID:{}  Обязательные дни:{}  Начало уроков:{}".format(self.id_user.id, self.required_days,
                                                                     self.time_start)
