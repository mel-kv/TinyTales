from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import CategoryListView, CategoryDetailView, SubcategoryDetailView, SubcategoryListView, ArticleDetailView, ArticleListView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("subcategories/", SubcategoryListView.as_view(), name="subcategory_list"),
    path(
        "subcategory/<int:pk>/",
        SubcategoryDetailView.as_view(),
        name="subcategory_detail",
    ),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

