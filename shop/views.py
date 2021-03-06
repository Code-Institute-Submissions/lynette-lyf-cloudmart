from django.shortcuts import render
from .models import Product, Origin
from wishlist.models import Wishlist
from django.contrib import messages
# from cart.views import calculate_cart_cost
from cart.views import view_cart_amount
from cart.models import CartItem


# Create your views here.


def catalog(request):
    # View all products
    products = Product.objects.all()
    # Pass in wishlist products to the catalog (list comprehension)
    print(request.user)
    wished_products = None
    if request.user.is_authenticated:
        wished_products = [ wished['product__id'] for wished in Wishlist.objects.filter(owner=request.user).values('product__id') ]
    print (wished_products)
    cart_amount = None
    if request.user.is_authenticated:
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/catalog.template.html',{
        'products': products,
        'wished_products': wished_products,
        'cart_amount': cart_amount
    })

# Filter product view by Origin
def catalog_japan(request):
    origin_search = Origin.objects.get(name='Japan')
    products = Product.objects.filter(origin=origin_search)
    cart_amount = None
    if request.user.is_authenticated:
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/catalog.template.html',{
        'products': products,
        'cart_amount': cart_amount
    })
    
def catalog_korea(request):
    origin_search = Origin.objects.get(name='Korea')
    products = Product.objects.filter(origin=origin_search)
    cart_amount = None
    if request.user.is_authenticated:
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/catalog.template.html',{
        'products': products,
        'cart_amount': cart_amount
    })
    
def catalog_taiwan(request):
    origin_search = Origin.objects.get(name='Taiwan')
    products = Product.objects.filter(origin=origin_search)
    cart_amount = None
    if request.user.is_authenticated:
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/catalog.template.html',{
        'products': products,
        'cart_amount': cart_amount
    })
    
# View individual product page
def productview(request, product_id):
    selected_product = Product.objects.get(pk=product_id)
    wished_products = None
    cart_amount = None
    if request.user.is_authenticated:
        wished_products = [ wished['product__id'] for wished in Wishlist.objects.filter(owner=request.user).values('product__id') ]
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/product_view.template.html', {
        'selected_product': selected_product,
        'wished_products': wished_products,
        'cart_amount': cart_amount
    })

# Allow wishlist buttons to be toggled on catalog
def toggleWishlist (request, product_id):
    wished_items = Wishlist.objects.filter(owner=request.user)
    all_products = Product.objects.all()
    cart_amount = None
    if request.user.is_authenticated:
        cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'shop/catalog.template.html', {
        'wished_items': wished_items,
        'all_products': all_products,
        'cart_amount': cart_amount
    })


