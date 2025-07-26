from django.contrib import admin

from .models import Book, Author, Address, Country

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_bestseller', 'slug')
    list_filter = ('is_bestseller', 'author', 'rating')
    readonly_fields = ('slug',)
    # prepopulated_fields = {'slug': ('title',)}

# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('user', 'street', 'city', 'postal_code')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)