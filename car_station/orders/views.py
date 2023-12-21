from django.shortcuts import render, redirect
from cars.models import Car
from orders.models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def buy_car (request, id):
    car = Car.objects.get(id = id)
    if car.quantity > 0:
        car.quantity -= 1
        order = Order()
        order.owner = request.user
        order.car = car
        order.save()
        car.save()
    return redirect('profile')