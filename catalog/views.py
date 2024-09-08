from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms import inlineformset_factory
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductFormCreate, ProductFormUpdate, ProductModeratorForm, VersionForm
from catalog.models import Category, Product, Version
from django.core.exceptions import PermissionDenied

from catalog.services import get_category_data


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, cur_ver=True).last()
            if active_version is None:
                active_version = 'Нет активной версии'
            product.active_version = active_version
        return context_data


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductFormCreate
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductFormUpdate

    def get_success_url(self):
        return reverse_lazy('catalog:product', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
        
    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductFormUpdate
        if user.has_perm('catalog.can_change_publicate') and user.has_perm('catalog.can_change_description_product') and user.has_perm('catalog.can_change_category_product'):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:products')

class CategoryListView(ListView):
    model = Category
    
    def get_queryset(self):
        return get_category_data()