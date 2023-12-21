from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Car
from .forms import CommentForm

# Create your views here.
class CarDetailsView (DetailView):
    model= Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post (self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        car = self.get_object()
        if request.method == 'POST':
            new_comment = comment_form.save(commit = False)
            new_comment.car = car
            new_comment.save()

        return self.get(self, request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form

        return context





