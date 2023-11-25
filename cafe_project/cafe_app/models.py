# cafe_app/models.py

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(MenuItem, related_name='categories')

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.author} - {self.rating} stars"

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    menu = models.ManyToManyField(MenuItem, related_name='cafes_menu')
    reviews = models.ManyToManyField(Review, related_name='cafes_reviews')

    def __str__(self):
        return self.name
