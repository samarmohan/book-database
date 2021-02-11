from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


GRADE_CHOICES = (
    ("K-2", "K-2"),
    ("3-5", "3-5"),
    ("6-8", "6-8"),
    ("9-12", "9-12"),
    ("Young Adult", "Young Adult")
)


class BookModel(models.Model):
    Name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Your FULL name")
    Email = models.EmailField(max_length=255, blank=False, null=False, verbose_name="Your SCHOOL email")
    Title = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name="Title of the book")
    Author = models.CharField(max_length=255, blank=False, null=False, verbose_name="Author of the book")
    Description = models.TextField(blank=True, null=True, verbose_name="Summary of the book (Optional)")
    PageCount = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of pages in the book (Optional)")
    ContainsBadWords = models.BooleanField(blank=True, null=True)
    GradeLevel = models.CharField(verbose_name="Grade Level of this book (Default is 6-8)", max_length=20, choices=GRADE_CHOICES, default="6-8", null=True, blank=True)
    Rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=False, blank=False, verbose_name="Rating out of 10")

