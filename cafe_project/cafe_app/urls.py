# cafe_app/urls.py

from django.urls import path
from .views import MenuItemList, MenuItemDetail, MenuCategoryList, ReviewList, CafeList

urlpatterns = [
    path('menu/', MenuItemList.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuItemDetail.as_view(), name='menu-detail'),
    path('categories/', MenuCategoryList.as_view(), name='category-list'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('cafes/', CafeList.as_view(), name='cafe-list'),
]
