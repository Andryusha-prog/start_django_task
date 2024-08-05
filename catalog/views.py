from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from catalog.models import Product


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

