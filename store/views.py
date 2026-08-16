from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, Order

# Create your views here.

def index(request):
    """Home page with featured products"""
    products = Product.objects.all()[:6]  # Show 6 products
    return render(request, 'store/index.html', {'products': products})

def shop(request):
    """Shop page with all products"""
    category = request.GET.get('category', 'all')
    if category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)
    return render(request, 'store/shop.html', {'products': products, 'category': category})

def product_detail(request, product_id):
    """Single product page"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product.html', {'product': product})

def cart(request):
    """Cart page"""
    return render(request, 'store/cart.html')

@csrf_exempt
def create_order(request):
    """Create order from cart"""
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create(
            items=data['items'],
            customer_name=data['name'],
            customer_email=data['email'],
            customer_address=data['address'],
            total=data['total']
        )
        return JsonResponse({'success': True, 'order_id': order.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Admin API endpoints
def get_products(request):
    """API to get all products"""
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

@csrf_exempt
def add_product(request):
    """API to add product"""
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            price=data['price'],
            category=data['category'],
            description=data.get('description', ''),
            image_url=data.get('image_url', ''),
            stock=data.get('stock', 10)
        )
        return JsonResponse({'success': True, 'id': product.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_product(request, product_id):
    """API to delete product"""
    if request.method == 'DELETE':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)