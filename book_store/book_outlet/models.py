from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

from .constants import BOOKS_DETAILS_PAGE


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_absolute_url(self):
        return reverse(BOOKS_DETAILS_PAGE, args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.author}), rating: {self.rating}, is_bestseller: {self.is_bestseller}, slug: {self.slug}"
