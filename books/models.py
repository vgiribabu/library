from django.db import models


class Library(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(' date_published')
