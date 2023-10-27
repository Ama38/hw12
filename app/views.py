from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from .forms import UpdateProductForm
from .models import *

# Create your views here.


class ProductListView(ListView):
    template_name = 'app/index.html'
    model = Product


class DeleteProductView(DeleteView):
    template_name = 'app/delete.html'
    success_url = reverse_lazy('product_list')
    model = Product
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class UpdateProductView(UpdateView):
    template_name = 'app/update.html'
    success_url = reverse_lazy('product_list')
    model = Product
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    form_class = UpdateProductForm
