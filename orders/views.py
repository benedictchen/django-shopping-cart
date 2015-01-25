from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from carts.models import Cart
from .models import Order
from .utils import OrderIdGenerator

@login_required
def checkout(request):
    try:
        cart_id = request.session['cart_id']
    except KeyError:
        return HttpResponseRedirect(reverse('view_cart'))
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        return HttpResponseRedirect(reverse('view_cart'))


    try:
        order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        order_id = OrderIdGenerator.generate_order_id()
        # TODO: Allow anonymous users to checkout
        order = Order(cart=cart, id=order_id, user=request.user)
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

@login_required
def orders(request):
    Order.objects.filter(user=request.user)
    context = {}
    template = 'orders.html'
    return render(request, template, context)
