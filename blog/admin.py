from django.contrib import admin
from .models import Post

# Register your models here my friend :3.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)


admin.site.register(Post, PostAdmin)
