from rest_framework import generics
from .models import MenuItem, MenuCategory, Review, Cafe
from .serializers import MenuItemSerializer, MenuCategorySerializer, ReviewSerializer, CafeSerializer
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView


class MenuItemList(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, NotFound):
        response_data = {'detail': 'Not found.'}
        response = Response(response_data, status=exc.status_code)

    return response


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuCategoryList(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CafeList(generics.ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
