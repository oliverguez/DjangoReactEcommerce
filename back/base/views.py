from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.


class GetProducts(APIView):
    def get(self, request, format=None):
        return Response(products)


class GetProduct(APIView):
    def get(self, request, pk):
        product = None
        for i in products:
            if i['_id'] == pk:
                product = i
                break
        return Response(product)


# class get_products(APIView):
#     def get(self, request):
#         return Response(products)


# @api_view('GET', 'POST', 'PUT', 'DELETE')
# def get_routes(request):
#     return Response('Hello', safe=False)
