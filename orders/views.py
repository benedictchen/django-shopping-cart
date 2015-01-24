import time
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from .models import Order


def checkout(request):
    try:
        cart_id = request.session['cart_id']
    except KeyError:
        return HttpResponseRedirect(reverse('view_cart'))
    cart = Cart.objects.get(id=cart_id)
    order, is_created = Order.objects.get_or_create(cart=cart)
    if is_created:
        order.order_id = str(time.time())
        order.save()

    if order.status == 'finished':
        try:
            del request.session['cart_id']
            del request.session['cart_count']
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('view_cart'))
    context = {
        'order': order
    }
    template = 'checkout.html'
    return render(request, template, context)

