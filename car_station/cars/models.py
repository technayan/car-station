from django.db import models
from brands.models import Brand

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.FileField(upload_to='cars/uploads/')
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.brand}'
    

class Comment(models.Model):
    name = models.CharField(max_length = 100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self):
        return f'Comment by - {self.name}'