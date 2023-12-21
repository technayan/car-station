from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .forms import RegistrationForm, ChangeUserForm
from django.urls import reverse_lazy
from orders.models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
class RegistrationView (CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context


class UserLoginView (LoginView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView (LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
    

def profileView (request):
    orders = Order.objects.filter(owner = request.user)
    cars = []
    for order in orders:
        cars.append(order.car)
    # cars = Car.objects.filter(id = orders[1].id)
    # cars = None

    return render(request, 'profile.html', {'cars' : cars})
    


@login_required
def edit_profile (request):
    if request.method == "POST":
        form = ChangeUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
        return redirect('profile')

    else:
        form = ChangeUserForm(instance = request.user)
    return render (request, 'form.html', {'form': form, 'type': 'Update'})



def change_password (req):
    if req.method == 'POST':
        form = PasswordChangeForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(user = req.user)
    return render (req, 'form.html', {'form': form, 'type': 'Update'})