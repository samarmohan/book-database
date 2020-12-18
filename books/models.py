from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BookResponse(models.Model):
    Name = models.CharField(max_length=255, blank=False, null=False)
    Email = models.EmailField(max_length=255, blank=False, null=False)
    Title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Author = models.CharField(max_length=255, blank=False, null=False)
    Description = models.TextField(blank=True, null=True)
    Rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
