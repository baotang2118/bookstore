from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import books, categories, authors, orders, books, \
    order_items, reviews, discounts


class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = [
            "id",
            "category_name",
            "category_desc",
        ]

class authorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = authors
        fields = [
            "id",
            "author_name",
            "author_bio",
        ]

class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = [
            "id",
            "order_date",
            "order_amount",
        ]

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = [
            "id",
            "category_id",
            "author_id",
            "book_title",
            "book_summary",
            "book_price",
            "book_cover_photo",
        ]

class order_itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_items
        fields = [
            "id",
            "order_id",
            "book_id",
            "quantity",
            "price",
        ]

class reviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields = [
            "id",
            "book_id",
            "review_title",
            "review_details",
            "review_date",
            "rating_star",
        ]

class discountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = discounts
        fields = [
            "id",
            "book_id",
            "discounts_start_date",
            "discounts_end_date",
            "discount_price",
        ]
