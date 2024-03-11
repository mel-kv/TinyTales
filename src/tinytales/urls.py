from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("bump/", include('bump_journal.urls')),
    path("baby/", include('baby_journal.urls')),
    path("", include('users.urls')),
    
]
