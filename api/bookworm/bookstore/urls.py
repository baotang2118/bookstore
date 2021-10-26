from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.req_books),
    path("book/<int:pk>/", views.req_book),
    path("categories/", views.req_categories),
    path("category/<int:pk>/", views.req_category),
    path("authors/", views.req_authors),
    path("author/<int:pk>/", views.req_author),
    path("orders/", views.req_orders),
    path("order/<int:pk>/", views.req_order),
    path("reviews/", views.req_reviews),
    path("review/<int:pk>/", views.req_review),
    path("discounts/", views.req_discounts),
    path("discount/<int:pk>/", views.req_discount),
]
