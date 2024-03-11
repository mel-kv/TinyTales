from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Category, Subcategory, Article




class CategoryListView(ListView):
    model = Category
    template_name = 'blog/categories/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/categories/category_detail.html'
    context_object_name = 'category'

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'blog/subcategories/subcategory_list.html'
    context_object_name = 'subcategories'

class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'blog/subcategories/subcategory_detail.html'
    context_object_name = 'subcategory'

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles/article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles/article_detail.html'
    context_object_name = 'article'
