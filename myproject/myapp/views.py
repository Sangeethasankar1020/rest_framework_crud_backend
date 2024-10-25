# myapp/views.py
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import db  # Import the MongoDB client

@csrf_exempt  # Disable CSRF protection for simplicity
@api_view(["GET"])
def get_products(request):
    products = list(db.products.find())  # Retrieve all products
    for product in products:
        product['_id'] = str(product['_id'])  # Convert ObjectId to string for JSON serialization
    return JsonResponse(products, safe=False)

@csrf_exempt
@api_view(["POST"])
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Get JSON data from request body
        new_product = {
            'name': data.get('name'),
            'description': data.get('description'),
            'price': data.get('price')
        }
        db.products.insert_one(new_product)  # Insert new product into MongoDB
        return JsonResponse({'message': 'Product added successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
