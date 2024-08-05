from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = ('tittle', 'slug', 'content', 'preview', 'create_date', 'publication',)
    success_url = reverse_lazy('blog:main')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.tittle)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('tittle', 'slug', 'content', 'preview', 'publication',)
    success_url = reverse_lazy('blog:main')

    def get_success_url(self):
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:main')
