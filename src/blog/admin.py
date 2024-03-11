from django.contrib import admin
from .models import Category, Subcategory, Article, Recipe, User


# Optional: Define custom admin classes to customize the admin interface

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'last_modified')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'prep_time', 'cook_time')
    list_filter = ('prep_time', 'cook_time', 'author')
    search_fields = ('title', 'ingredients', 'instructions')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'content_type', 'object_id', 'caption')
    readonly_fields = ('image_tag',)

# # class UserProfileAdmin(admin.ModelAdmin):
# #     list_display = ('user', 'role')
# #     list_filter = ('role',)

# # Register your models here
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Recipe, RecipeAdmin)

# # admin.site.register(UserProfile, UserProfileAdmin)


# # If you need to customize the User model's admin, you can unregister it and then re-register with your customizations.
# # admin.site.unregister(User)
# # admin.site.register(User, CustomUserAdmin)
