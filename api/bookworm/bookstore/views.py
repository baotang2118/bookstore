from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import categories, authors, orders
from .serializers import categoriesSerializer, authorsSerializer, ordersSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def book(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass

@api_view(['GET', 'POST'])
def req_categories(request):
    if request.method == 'GET':
        data = categories.objects.all()
        serializer = categoriesSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = categoriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def req_category(request, pk):
    data = categories.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = categoriesSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        serializer = categoriesSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def req_authors(request):
    if request.method == 'GET':
        data = authors.objects.all()
        serializer = authorsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = authorsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def req_author(request, pk):
    data = authors.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = authorsSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        serializer = authorsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def req_orders(request):
    if request.method == 'GET':
        data = orders.objects.all()
        serializer = ordersSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ordersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def req_order(request, pk):
    data = orders.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ordersSerializer(data)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        serializer = ordersSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)

@api_view(['POST'])
def create_review(request):
    pass

@api_view(['POST'])
def update_review(request):
    pass

@api_view(['POST'])
def delete_review(request):
    pass

@api_view(['GET'])
def get_reviews(request):
    pass

@api_view(['POST'])
def create_discount(request):
    pass

@api_view(['POST'])
def update_discount(request):
    pass

@api_view(['POST'])
def delete_discount(request):
    pass

@api_view(['GET'])
def get_discounts(request):
    pass

@api_view(['POST'])
def create_order_item(request):
    pass

@api_view(['POST'])
def update_order_item(request):
    pass

@api_view(['POST'])
def delete_order_item(request):
    pass

@api_view(['GET'])
def get_order_items(request):
    pass