from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'tags', 'date')
    list_display = ('title', 'date', 'author')
    readonly_fields = ('slug',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)