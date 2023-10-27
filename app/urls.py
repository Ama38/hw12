from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update_product')
]