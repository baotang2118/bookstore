from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class books(models.Model):
    category_id = models.ManyToManyField('categories')
    author_id = models.ManyToManyField('authors')
    book_title = models.TextField()
    book_summary = models.TextField()
    book_price = models.DecimalField(max_digits=5, decimal_places=2)
    book_cover_photo = models.CharField(max_length=20)

    def __str__(self):
        return self.book_title

class categories(models.Model):
    category_name = models.CharField(max_length=120)
    category_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class authors(models.Model):
    author_name = models.TextField()
    author_bio = models.TextField()

    def __str__(self):
        return self.author_name

class reviews(models.Model):
    book_id = models.ForeignKey(books, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=120)
    review_details = models.TextField()
    review_date = models.TimeField()
    star = models.TextChoices("star", "1 2 3 4 5") 
    rating_star = models.CharField(blank=True, choices=star.choices, max_length=3)

    def __str__(self):
        return self.review_title

class discounts(models.Model):
    book_id = models.OneToOneField(books, on_delete=models.CASCADE)
    discounts_start_date = models.DateField()
    discounts_end_date = models.DateField()
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)

class orders(models.Model):
    order_date = models.TimeField()
    order_amount = models.DecimalField(max_digits=5, decimal_places=2)

class order_items(models.Model):
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)
    book_id = models.OneToOneField(books, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

