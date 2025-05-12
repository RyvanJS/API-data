# Blog/filters.py

from django_filters import rest_framework as filters
from .models import BlogPost

class BlogPostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BlogPost
        fields = ['title']
