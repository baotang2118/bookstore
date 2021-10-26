from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import categories, authors, orders, books, order_items, reviews, discounts
from .serializers import categoriesSerializer, authorsSerializer, ordersSerializer, \
    booksSerializer, order_itemsSerializer, reviewsSerializer, discountsSerializer

# Create your views here.


@api_view(["GET", "POST"])
def req_books(request):
    if request.method == "GET":
        data = books.objects.all()
        serializer = booksSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = booksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])
def req_book(request, pk):
    data = books.objects.get(pk=pk)
    if request.method == "GET":
        serializer = booksSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = booksSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)

@api_view(["GET", "POST"])
def req_categories(request):
    if request.method == "GET":
        data = categories.objects.all()
        serializer = categoriesSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = categoriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_category(request, pk):
    data = categories.objects.get(pk=pk)
    if request.method == "GET":
        serializer = categoriesSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = categoriesSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)


@api_view(["GET", "POST"])
def req_authors(request):
    if request.method == "GET":
        data = authors.objects.all()
        serializer = authorsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = authorsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_author(request, pk):
    data = authors.objects.get(pk=pk)
    if request.method == "GET":
        serializer = authorsSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = authorsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)


@api_view(["GET", "POST"])
def req_orders(request):
    if request.method == "GET":
        data = orders.objects.all()
        serializer = ordersSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ordersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_order(request, pk):
    data = orders.objects.get(pk=pk)
    if request.method == "GET":
        serializer = ordersSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = ordersSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)

@api_view(["GET", "POST"])
def req_order_items(request):
    if request.method == "GET":
        data = order_items.objects.all()
        serializer = order_itemsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = order_itemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_order_items(request, pk):
    data = order_items.objects.get(pk=pk)
    if request.method == "GET":
        serializer = order_itemsSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = order_itemsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)

@api_view(["GET", "POST"])
def req_reviews(request):
    if request.method == "GET":
        data = reviews.objects.all()
        serializer = reviewsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = reviewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_review(request, pk):
    data = reviews.objects.get(pk=pk)
    if request.method == "GET":
        serializer = reviewsSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = reviewsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)

@api_view(["GET", "POST"])
def req_discounts(request):
    if request.method == "GET":
        data = discounts.objects.all()
        serializer = discountsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = discountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def req_discount(request, pk):
    data = discounts.objects.get(pk=pk)
    if request.method == "GET":
        serializer = discountsSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        json_data = JSONParser().parse(request)
        serializer = discountsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse(status=204)
