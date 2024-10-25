# myapp/views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId  # For handling MongoDB ObjectId
from .db import db  # Import the MongoDB client
import json

@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all products or create a new product.
    """
    if request.method == 'GET':
        products = list(db.products.find())
        for product in products:
            product['_id'] = str(product['_id'])  # Convert ObjectId to string for JSON serialization
        return Response(products)

    elif request.method == 'POST':
        data = request.data
        new_product = {
            'name': data.get('name'),
            'description': data.get('description'),
            'price': data.get('price')
        }
        db.products.insert_one(new_product)  # Insert new product into MongoDB
        return Response({'message': 'Product added successfully!'}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update, or delete a product by id.
    """
    # Convert pk to ObjectId
    try:
        product = db.products.find_one({"_id": ObjectId(pk)})
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Invalid product ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        product['_id'] = str(product['_id'])  # Convert ObjectId to string for JSON serialization
        return Response(product)

    elif request.method == 'PUT':
        data = request.data
        updated_product = {
            'name': data.get('name', product['name']),
            'description': data.get('description', product['description']),
            'price': data.get('price', product['price'])
        }
        db.products.update_one({'_id': ObjectId(pk)}, {'$set': updated_product})
        return Response({'message': 'Product updated successfully!'})

    elif request.method == 'DELETE':
        db.products.delete_one({'_id': ObjectId(pk)})
        return Response({'message': 'Product deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
