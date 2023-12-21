from django.urls import path
from . import views

urlpatterns = [
    path('car-details/<int:id>/', views.CarDetailsView.as_view(), name="car_details"),
]
