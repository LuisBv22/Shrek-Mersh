from django.shortcuts import redirect, get_object_or_404, render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'merchapp/all_products.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = {Product.objects.get(id=pid): quantity for pid, quantity in cart.items()}
    total = sum([product.price * quantity for product, quantity in cart_items.items()])
    return render(request, 'cart.html', {'cart': cart_items, 'total': total})
