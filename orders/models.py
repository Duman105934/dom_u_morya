from django.db import models
from houses.models import House


class Order(models.Model):
    house = models.ForeignKey(House, verbose_name="дом", on_delete=models.CASCADE)
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    date = models.DateTimeField("дата", auto_now_add=True)