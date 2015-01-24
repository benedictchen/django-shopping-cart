from django.contrib.auth.models import User
from django.db import models
from products.models import Product, Variation


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Cart #' + unicode(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True)
    product = models.ForeignKey(Product)
    variations = models.ManyToManyField(Variation, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Order #' + unicode(self.id) + ' of ' + self.product.title

