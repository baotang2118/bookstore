from django.db import router
from django.db.models import base
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'order_items', views.order_items_viewset, basename='order_item')
router.register(r'reviews', views.req_reviews_ViewSet, basename='reviews')
router.register(r'discounts', views.req_discounts_ViewSet)

urlpatterns = [
    path("books/", views.req_books),
    path("books/<int:pk>/", views.req_book),
    path("categories/", views.req_categories.as_view()),
    path("categories/<int:pk>/", views.req_category.as_view()),
    path("authors/", views.req_authors.as_view()),
    path("authors/<int:pk>/", views.req_author.as_view()),
    path("orders/", views.req_orders.as_view()),
    path("orders/<int:pk>/", views.req_order.as_view()),
    
    # path("reviews/", views.req_reviews),
    # path("reviews/<int:pk>/", views.req_review),
    # path("discounts/", views.req_discounts),
    # path("discounts/<int:pk>/", views.req_discount),

    path("delete_authors/", views.ajax_delete_authors.as_view())
]

urlpatterns += router.urls
