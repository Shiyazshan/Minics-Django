from django.shortcuts import render
from product.models import Product,Cart,CartItem


def product(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, "product.html", context=context)


def cart(request):
    items = Cart.objects.all()

    context = {
        'items' : items,
    }

    return render(request, "cart.html", context=context)

def update_cart(request,slug):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not product in cart.products.all():
        cart.products.add(cart_item)
    else:
        cart.products.remove(cart_item)

    # new_total = 0.00
    # for item in cart.items.all():
    #     line_total = (item.product.price) = item.quantity
    #     new_total += line_total
    
    # request.session['items_total'] = cart.items.count()
    # cart.total = new_total
    # cart.save()

    # return render(request, "cart.html")




    