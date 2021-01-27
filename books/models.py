from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BookResponse(models.Model):
    Name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Your FULL name")
    Email = models.EmailField(max_length=255, blank=False, null=False, verbose_name="Your SCHOOL email")
    Title = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name="Title of the book")
    Author = models.CharField(max_length=255, blank=False, null=False, verbose_name="Author of the book")
    Description = models.TextField(blank=True, null=True, verbose_name="Summary of the book (Optional)")
    PageCount = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of pages in the book (Optional)")
    ContainsBadWords = models.BooleanField(verbose_name="Does this book contain bad words? (Bad for an 8 year old)", null=True, blank=True)
    Rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=False, blank=False, verbose_name="Rating out of 10")

