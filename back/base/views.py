from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from .products import products
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import ProductSerializer

# Create your views here.


class GetProducts(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class GetProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(_id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


# class get_products(APIView):
#     def get(self, request):
#         return Response(products)


# @api_view('GET', 'POST', 'PUT', 'DELETE')
# def get_routes(request):
#     return Response('Hello', safe=False)
