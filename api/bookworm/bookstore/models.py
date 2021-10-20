from django.db import models

# Create your models here.

class book(models.Model):
    category_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    book_title = models.TextField()
    book_summary = models.TextField()
    book_price = models.DecimalField(max_digits=5, decimal_places=2)
    book_cover_photo = models.CharField(max_length=20)

class categories(models.Model):
    category_name = models.CharField(max_length=120)
    category_desc = models.CharField(max_length=255)

class authors(models.Model):
    author_name = models.TextField()
    author_bio = models.TextField()

class reviews(models.Model):
    book_id = models.BigIntegerField()
    review_title = models.CharField(max_length=120)
    review_details = models.TextField()
    review_date = models.TimeField()
    rating_star = models.TextChoices('1','2','3','4','5')

class discounts(models.Model):
    book_id = models.BigIntegerField()
    discounts_start_date = models.DateField()
    discounts_end_date = models.DateField()
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)

class order_items(models.Model):
    order_id = models.BigIntegerField()
    book_id = models.BigIntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

class orders(models.Model):
    order_date = models.TimeField()
    order_amount = models.DecimalField(max_digits=5, decimal_places=2)
