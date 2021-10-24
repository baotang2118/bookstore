from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book),
    path('categories/', views.req_categories),
    path('category/<int:pk>/', views.req_category),
    path('authors/', views.req_authors),
    path('author/<int:pk>/', views.req_author),
    path('orders/', views.req_orders),
    path('order/<int:pk>/', views.req_order),
]
