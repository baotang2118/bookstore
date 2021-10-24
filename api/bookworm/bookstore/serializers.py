from rest_framework import serializers
from .models import categories, authors, orders

class categoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=120)
    category_desc = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return categories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_desc)
        instance.category_desc = validated_data.get('category_desc', instance.category_desc)
        instance.save()
        return instance

class authorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_name = serializers.TextField()
    author_bio = serializers.TextField()

    def create(self, validated_data):
        return authors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.author_bio = validated_data.get('author_bio', instance.author_bio)
        instance.save()
        return instance

class ordersSerializer(serializers.Serializer):
    order_date = serializers.TimeField()
    order_amount = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        return orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.order_amount = validated_data.get('order_amount', instance.order_amount)
        instance.save()
        return instance

# class discountsSerializer(serializers.Serializer):
#     book_id = models.OneToOneField(books, on_delete=models.CASCADE)
#     discounts_start_date = models.DateField()
#     discounts_end_date = models.DateField()
#     discount_price = models.DecimalField(max_digits=5, decimal_places=2)
