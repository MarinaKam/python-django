from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

from .constants import BOOKS_DETAILS_PAGE

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    def __str__(self):
        return self.full_address()


    class Meta:
        verbose_name_plural = "Address"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(max_length=100, null=True, blank=True)
    # if we remove author all related books will be deleted also
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')

    # if we remove author there will be error
    # author = models.ForeignKey(Author, on_delete=models.PROTECT)

    # if we remove author, in his books the author field became NULL
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name='books')

    def __str__(self):
        # return f"{self.title} ({self.author}), rating: {self.rating}, is_bestseller: {self.is_bestseller}, slug: {self.slug}"
        return f"{self.title} ({self.author})"

    def get_absolute_url(self):
        return reverse(BOOKS_DETAILS_PAGE, args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

