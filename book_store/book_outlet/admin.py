from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_bestseller', 'slug')
    list_filter = ('is_bestseller', 'author', 'rating')
    readonly_fields = ('slug',)
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)