from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('articles/', BlogListView.as_view(), name='main'),
    path('article/<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]
