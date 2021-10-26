from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import books, categories, authors, orders, books, \
    order_items, reviews, discounts


class categoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=120)
    category_desc = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return categories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get(
            "category_name", instance.category_name
        )
        instance.category_desc = validated_data.get(
            "category_desc", instance.category_desc
        )
        instance.save()
        return instance


class authorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_name = serializers.CharField()
    author_bio = serializers.CharField()

    def create(self, validated_data):
        return authors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author_name = validated_data.get("author_name", instance.author_name)
        instance.author_bio = validated_data.get("author_bio", instance.author_bio)
        instance.save()
        return instance


class ordersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_date = serializers.IntegerField()
    order_amount = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        return orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get("order_date", instance.order_date)
        instance.order_amount = validated_data.get(
            "order_amount", instance.order_amount
        )
        instance.save()
        return instance


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
        depth = 1

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
        depth = 1

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
        depth = 1

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
        depth = 1
