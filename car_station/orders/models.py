from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.owner} - {self.car}'