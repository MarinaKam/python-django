from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.author}), rating: {self.rating}, is_bestseller: {self.is_bestseller}"
