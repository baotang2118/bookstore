from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import categories, authors, orders, books, order_items, reviews, discounts
from .serializers import categoriesSerializer, authorsSerializer, ordersSerializer, \
    booksSerializer, order_itemsSerializer, reviewsSerializer, discountsSerializer

# Create your views here.

# s3p3McQ9WJH2L3L

# Function based view

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
    try:
        data = books.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
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

# Class based view

class req_categories(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
        }
# curl -X GET http://localhost:8000/bookstore/categories/ -H 'Authorization: Token 56aa0e127bf13102525f6320e4b7e5c0f9f7b8b9'
        data = categories.objects.all()
        serializer = categoriesSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = categoriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class req_category(APIView):
    def get_category(self, pk):
        try:
            return categories.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request, pk, format=None):
            data = self.get_category(pk)
            serializer = categoriesSerializer(data)
            return JsonResponse(serializer.data)
    def put(self, request, pk, format=None):
            json_data = JSONParser().parse(request)
            data = self.get_category(pk)
            serializer = categoriesSerializer(data, json_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
            data = self.get_category(pk)
            data.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Mixins based view

class req_authors(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication ]
    permission_classes = [IsAuthenticated]
    
    queryset = authors.objects.all()
    serializer_class = authorsSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class req_author(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = authors.objects.all()
    serializer_class = authorsSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ajax_delete_authors(APIView):
    def get(self, request, format=None):
        return render(request, 'delete_authors.html')

# Generics based view

class req_orders(generics.ListCreateAPIView):
    queryset = orders.objects.all()
    serializer_class = ordersSerializer

class req_order(generics.RetrieveUpdateDestroyAPIView):
    queryset = orders.objects.all()
    serializer_class = ordersSerializer

# Viewset, router need basename

class order_items_viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = order_items.objects.all()
        serializer = order_itemsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        queryset = JSONParser().parse(request)
        serializer = order_itemsSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        queryset = order_items.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = order_itemsSerializer(data)
        return JsonResponse(serializer.data)

    def update(self, request, pk=None):
        json_data = JSONParser().parse(request)
        queryset = order_items.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = order_itemsSerializer(data, json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        return HttpResponse(status=404)

    def destroy(self, request, pk=None):
        queryset = order_items.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        data.delete()
        return HttpResponse(status=204)

# GenericViewset

class req_reviews_ViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = reviews.objects.all()
    serializer_class = reviewsSerializer

# ModelViewset

class req_discounts_ViewSet(viewsets.ModelViewSet):
    queryset = discounts.objects.all()
    serializer_class = discountsSerializer
