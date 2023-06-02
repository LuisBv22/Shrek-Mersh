from . import views
from django.urls import path
from .views import add_to_cart
from .views import view_cart

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
]