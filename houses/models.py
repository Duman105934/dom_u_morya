from django.db import models


class House(models.Model):
    name = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
    photo = models.ImageField("фотография", upload_to="houses/photos", default="", blank=True)
    active = models.BooleanField("активен", default=True)

    class Meta:
        verbose_name = "дом"
        verbose_name_plural = "дома"
        ordering = ["-active","name"]

    def __str__(self):
        return self.name