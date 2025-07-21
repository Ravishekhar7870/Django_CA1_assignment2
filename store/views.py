from django.shortcuts import render
from django.http import HttpResponse
from django.template import TemplateDoesNotExist

# Fake database
products = {
    101: {'title': 'C++ Book', 'price': 499, 'description': 'A great book on C++.'},
    102: {'title': ' Mug', 'price': 299, 'description': 'A mug for daily usage.'},
    103: {'title': ' Black Salt', 'price': 50, 'description': '100g black salt of great quality.'}
}

# 1. Home View
def home_view(request):
    featured = [products[101], products[102]]
    return render(request, 'home.html', {'featured': featured})

# 2. Product Detail View by ID
def product_detail(request, id):
    product = products.get(id)
    if not product:
        return render(request, '404.html', status=404)
    return render(request, 'product.html', {'product': product})

# 3. Product Detail View by slug (regex)
def product_slug_view(request, slug):
    for product in products.values():
        if slug == product['title'].lower().replace(' ', '-'):
            return render(request, 'product.html', {'product': product})
    return render(request, '404.html', status=404)

# 4. Simulated Add to Cart
def add_to_cart(request, id):
    product = products.get(id)
    if not product:
        return HttpResponse("Product not found", status=404)
    cart = request.session.get('cart', [])
    cart.append(product['title'])
    request.session['cart'] = cart
    return render(request, 'cart.html', {'product_name': product['title']})
