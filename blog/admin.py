from django.contrib import admin
from .models import Post, Category, PostImage

# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageAdmin]

    class Meta:
        model = Post
    
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)