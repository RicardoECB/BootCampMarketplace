from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ProductSerializer, PhotoSerializer, TagSerializer, CategorySerializer
from .models import Product, Photo, Tag, Category

class ProtectedView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        serializer = UserSerializer(request.user)
        return Response(
            serializer.data
        )

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer

class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoCreateAPIView(CreateAPIView):
    serializer_class = PhotoSerializer

class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagCreateAPIView(CreateAPIView):
    serializer_class = TagSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
