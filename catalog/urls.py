from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, single_product, all_products

app_name = CatalogConfig.name

urlpatterns = [
    #path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', single_product, name='product'),
    path('', all_products, name='products')
]
