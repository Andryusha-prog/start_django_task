from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, HomePageView, ContactsPageView, ProductDetailView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('', ProductListView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('category/', CategoryListView.as_view(), name='category'),
]
