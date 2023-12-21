from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from cars.models import Car
from brands.models import Brand
from django.urls import reverse_lazy

def home (request, brand_slug = None):
    cars = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand = brand)
    brands = Brand.objects.all()

    return render (request, 'index.html', {'cars': cars, 'brands': brands, 'slug': brand_slug})

# class HomeView (ListView):
#     model = Car
#     template_name = 'index.html'
#     success_url = reverse_lazy('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(pk_url_kwarg)

#         context['cars'] = Car.objects.all()
#         context['brands'] = Brand.objects.all()
#         return context
    
