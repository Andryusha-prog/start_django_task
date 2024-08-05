from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomePageView, ContactsPageView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('', ProductListView.as_view(), name='products')
]
