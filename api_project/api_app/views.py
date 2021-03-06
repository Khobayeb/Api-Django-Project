from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status

from api_app import serializer


# Create your views here.

def home(request):
    list= Product.objects.all()
    context={
        'products':list
    }
    return render(request,'home.html', context)
@api_view(['GET', 'POST'])
def product(request):
    if request.method== "GET":
        list = Product.objects.all()
        serializer= ProductSerializer(list,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def productDetails(request,pk):
    try:
       list = Product.objects.get(id= pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method== "GET":


        serializer= ProductSerializer(list)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer= ProductSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



